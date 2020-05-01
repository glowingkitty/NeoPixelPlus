import math
import random
import time


class NeoPixel:
    def __init__(self,
                 pin_num=10,
                 n=30,
                 bpp=3,
                 start_point=0,
                 brightness=0.9,
                 test=False,
                 animation_up_and_down=True,
                 animation_direction='up'):
        self.strip_length = n
        self.time_passed = 0
        self.brightness = brightness
        self.start_point = start_point
        self.test = test
        self.pin_num = pin_num
        self.animation_up_and_down = animation_up_and_down
        self.animation_direction = animation_direction
        if self.test:
            self.leds = [[0, 0, 0] for x in range(self.strip_length)]
        else:
            from neopixel import NeoPixel as NeoPixelOriginal
            from machine import Pin
            self.leds = NeoPixelOriginal(
                pin=Pin(pin_num, Pin.OUT),
                n=self.strip_length,
                bpp=bpp)

    def write(self, wait_after_wait=1.0/36.0):
        if self.test:
            from colr import color
            print(
                ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds))
        else:
            self.leds.write()
        time.sleep(wait_after_wait)

    def get_led(self, i):
        i = i+self.start_point
        if i < 0:
            i = self.strip_length+i
        return i

    def off(self):
        for i in range(self.strip_length):
            self.leds[i] = (0, 0, 0)
        self.write()

    def on(self, num=None):
        if type(num) == int:
            num = self.get_led(num)
            self.leds[num] = (255, 255, 255)
        else:
            for i in range(self.strip_length):
                self.leds[i] = (255, 255, 255)
        self.write()

    def random_flashing(self):
        while True:
            self.leds = [
                (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)) for x in range(self.strip_length)]
            self.write()

    def testing(self):
        # testing the LEDs
        if self.test:
            print('Start simulating a test of a NeoPixel LED strip.')
        else:
            print('Start testing a NeoPixel LED strip')

        print('pin: {}'.format(self.pin_num))
        print('strip_length: {}'.format(self.strip_length))

        time.sleep(2)

        self.glowup_and_down(limit=30)
        self.count_glowing()
        self.rainbow_animation(limit=50)

    def count_glowing(self):
        counter = 0
        while counter < self.strip_length:
            print('This is LED No {}'.format(counter))
            for i in range(self.strip_length):
                if i != counter:
                    i = self.get_led(i)
                    self.leds[i] = (0, 0, 0)
                else:
                    i = self.get_led(i)
                    self.leds[i] = (255, 255, 255)

            self.write()
            time.sleep(0.5)
            counter += 1

    def glowup_and_down(self, limit=None):
        counter = 0
        while True:
            for i in range(self.strip_length):
                i = self.get_led(i)
                if self.leds[i] == (0, 0, 0):
                    self.leds[i] = (255, 0, 0)
                else:
                    self.leds[i] = (0, 0, 0)
            self.write()

            counter += 1
            if limit and counter == limit:
                break
            time.sleep(0.1)

    def rainbow_animation(self, limit=None):
        # turn LEDs rainbow
        counter = 0
        while True:
            self.time_passed += 0.06
            for i in range(self.strip_length):
                i = self.get_led(i)
                color = self.rainbow_color(self.time_passed, i,
                                           self.brightness)
                self.leds[i] = color

            if self.animation_up_and_down:
                self.brightness, self.animation_direction = self.change_brightness(
                    self.brightness, self.animation_direction)

            self.write()

            counter += 1
            if limit and counter == limit:
                break

    def rainbow_color(self, t, i, brightness):
        a = (0.5, 0.5, 0.5)
        b = (0.5, 0.5, 0.5)
        c = (1.0, 1.0, 1.0)
        d = (0.00, 0.33, 0.67)

        k = t + 0.05 * i

        r = a[0] + b[0] * math.cos(6.28318 * (c[0] * k + d[0]))
        g = a[1] + b[1] * math.cos(6.28318 * (c[1] * k + d[1]))
        b = a[2] + b[2] * math.cos(6.28318 * (c[2] * k + d[2]))

        return (int(255.0 * r * brightness), int(255.0 * g * brightness), int(255.0 * b * brightness))

    def change_brightness(self, brightness, direction):
        if direction == 'up':
            brightness = brightness + 0.025
        else:
            brightness = brightness - 0.025

        if brightness <= 0.1:
            direction = 'up'
        elif brightness >= 0.7:
            direction = 'down'

        return brightness, direction
