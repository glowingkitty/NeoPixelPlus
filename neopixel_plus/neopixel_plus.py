import math
import random
import time

from neopixel_plus.animations.beats_up_and_down import BeatsUpAndDown
from neopixel_plus.animations.rainbow import RainbowAnimation


class NeoPixel:
    def __init__(self,
                 pin_num=10,
                 n=30,
                 bpp=3,
                 start_point=0,
                 test=False,
                 ):
        self.strip_length = n
        self.start_point = start_point
        self.test = test
        self.pin_num = pin_num
        if self.test:
            self.leds = [[0, 0, 0] for x in range(self.strip_length)]
        else:
            from machine import Pin
            from neopixel import NeoPixel as NeoPixelOriginal
            self.leds = NeoPixelOriginal(
                pin=Pin(pin_num, Pin.OUT),
                n=self.strip_length,
                bpp=bpp)

    def write(self, s_after_wait=1.0/36.0):
        if self.test:
            from colr import color
            print(
                ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds))
        else:
            self.leds.write()
        time.sleep(s_after_wait)

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

    def color(self, r, g, b):
        for i in range(self.strip_length):
            i = self.get_led(i)
            self.leds[i] = (r, g, b)
        self.write()

    def rainbow_animation(self, loop_limit=None, brightness=1, duration_ms=1000, pause_ms=None):
        RainbowAnimation(
            led_strip=self,
            loop_limit=loop_limit,
            brightness=brightness,
            duration_ms=duration_ms,
            pause_ms=pause_ms
        ).glow()

    def beats(self, r=None, g=None, b=None, brightness=1, loop_limit=None, duration_ms=200, pause_ms=300, direction='up'):
        BeatsUpAndDown(
            led_strip=self,
            color=[r, g, b] if (r and g and b) else None,
            brightness=brightness,
            loop_limit=loop_limit,
            duration_ms=duration_ms,
            pause_ms=pause_ms,
            direction=direction
        ).glow()
