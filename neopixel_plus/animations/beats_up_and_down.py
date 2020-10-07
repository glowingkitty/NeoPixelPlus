import random
import time


class BeatsUpAndDown:
    def __init__(self, led_strip, color=None, brightness=1, loop_limit=None, duration_ms=200, pause_ms=300, direction='up'):
        self.led_strip = led_strip
        self.color = color if color else self.get_random_color()
        self.change_color_random = False if color else True
        self.brightness = brightness
        self.loop_limit = loop_limit
        self.duration_ms = duration_ms
        self.pause_ms = pause_ms
        self.direction = direction

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.strip_length)/1000

    def get_random_color(self):
        return [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    def set_color_brightness(self):
        r = int(self.color[0] * self.brightness)
        g = int(self.color[1] * self.brightness)
        b = int(self.color[2] * self.brightness)

        self.color = [r if r < 255 else 255, g if g <
                      255 else 255, b if b < 255 else 255]

    def glow(self):
        # make sure leds are off
        self.led_strip.off()

        while True:
            # update color if brightness different
            if self.brightness != 1:
                self.set_color_brightness()

            # color LEDs
            for i in range(self.led_strip.strip_length):
                if self.direction == 'down':
                    i = -(i+1)
                i = self.led_strip.get_led(i)
                self.led_strip.leds[i] = self.color

                self.led_strip.write(s_after_wait=self.write_wait_time)

            # then make them black
            for i in range(self.led_strip.strip_length):
                if self.direction == 'up':
                    i = -(i+1)
                i = self.led_strip.get_led(i)
                self.led_strip.leds[i] = [0, 0, 0]

                self.led_strip.write(s_after_wait=self.write_wait_time)

            # change color if color supposed to be random
            if self.change_color_random:
                self.color = self.get_random_color()

            if self.pause_ms:
                time.sleep(self.pause_ms/1000)
