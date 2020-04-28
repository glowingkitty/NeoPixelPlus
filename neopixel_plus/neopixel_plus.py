import math
import random
import time

from colr import color


class NeoPixel:
    def __init__(self, pin=10, n=30, bpp=3, brightness=0.9, auto_write=True, pixel_order=None, test=False, animation_up_and_down=True, animation_direction='up'):
        self.strip_length = n
        self.time_passed = 0
        self.brightness = brightness
        self.test = test
        self.animation_up_and_down = animation_up_and_down
        self.animation_direction = animation_direction
        if self.test:
            self.leds = [[0, 0, 0] for x in range(self.strip_length)]
        else:
            from neopixel import NeoPixel
            from machine import Pin
            self.leds = NeoPixel(
                pin=Pin(pin, Pin.OUT),
                n=self.strip_length,
                bpp=bpp,
                brightness=self.brightness,
                auto_write=auto_write,
                pixel_order=pixel_order)

    def write(self,wait_after_wait=1.0/36.0):
        if self.test:
            print(
                ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds))
        else:
            self.leds.write()
        time.sleep(wait_after_wait)

    def random_flashing(self):
        while True:
            self.leds = [
                (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)) for x in range(self.strip_length)]
            self.write()

    def rainbow_animation(self,loop=True):
        # turn LEDs rainbow
        while True:
            self.time_passed += 0.06
            for i in range(len(self.leds)):
                color = self.rainbow_color(self.time_passed, i,
                                        self.brightness)
                self.leds[i] = color

            if self.animation_up_and_down:
                self.brightness, self.animation_direction = self.change_brightness(
                    self.brightness, self.animation_direction)
            
            self.write()
            
            if not loop:
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
