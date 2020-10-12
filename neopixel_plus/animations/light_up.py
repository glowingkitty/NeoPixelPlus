import random
import time


class LightUp:
    def __init__(self,
                 led_strip,
                 color=None,
                 brightness=1,
                 brightness_fixed=False,
                 loop_limit=None,
                 duration_ms=200,
                 pause_ms=200,
                 direction='up'):
        self.led_strip = led_strip
        self.color = color if color else self.get_random_color()
        self.base_color = self.color
        self.change_color_random = False if color else True
        self.brightness = brightness
        self.brightness_max = brightness
        self.brightness_fixed = brightness_fixed
        self.loop_limit = loop_limit
        self.duration_ms = duration_ms
        self.pause_a_ms = pause_a_ms
        self.pause_b_ms = pause_b_ms
        self.direction = direction
        self.selector = {
            "up": [-1, -2, -3, -4, -5],
            "down": [0, 1, 2, 3, 4]
        }

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.strip_length)/1000

    def get_random_color(self):
        return [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    def set_color_brightness(self):
        r = int(self.base_color[0] * self.brightness)
        g = int(self.base_color[1] * self.brightness)
        b = int(self.base_color[2] * self.brightness)

        self.color = [r if r < 255 else 255, g if g <
                      255 else 255, b if b < 255 else 255]

    def glow(self):
        # make sure leds are off
        self.led_strip.off()

        # while True:
