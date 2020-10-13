import math
import random
import time
from random import randint

from neopixel_plus.animations import *


class NeoPixel:
    def __init__(self,
                 pin_num=10,
                 n=30,
                 bpp=3,
                 start_point=0,
                 test=False,
                 overwrite_line=True
                 ):
        self.strip_length = n
        self.addressable_strip_length = n
        self.start_point = start_point
        self.test = test
        self.pin_num = pin_num
        self.overwrite_line = overwrite_line
        self.sections = self.get_sections()
        if self.test:
            self.leds = [[0, 0, 0] for x in range(self.strip_length)]
        else:
            from machine import Pin
            from neopixel import NeoPixel as NeoPixelOriginal
            self.leds = NeoPixelOriginal(
                pin=Pin(pin_num, Pin.OUT),
                n=self.strip_length,
                bpp=bpp)

    def get_sections(self):
        sections_length = 15
        sections = []
        counter = 0
        while counter < self.addressable_strip_length:
            sections.append(
                [x for x in range(counter, counter+sections_length)])
            counter += sections_length
        return sections

    def get_led_selectors(self, sections='all'):
        if type(sections) == str and sections == 'all':
            return range(self.addressable_strip_length)
        else:
            selected_leds = []

            if sections == 'random':
                selected_leds += self.sections[randint(0,
                                                       len(self.sections)-1)]

            else:
                for entry in sections:
                    selected_leds += self.sections[entry]

            return selected_leds

    def write(self, s_after_wait=1.0/36.0):
        if self.test:
            from colr import color
            print(
                ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds), end='\r' if self.overwrite_line else '\n')
        else:
            self.leds.write()
        time.sleep(s_after_wait)

    def get_led(self, i, direction=None):
        i = i+self.start_point
        if i < 0:
            i = self.addressable_strip_length+i
        if direction and direction == 'down':
            i += (self.strip_length-self.addressable_strip_length)
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

    def rainbow_animation(self,
                          loop_limit=None,
                          brightness=1,
                          duration_ms=1000,
                          pause_ms=None):
        RainbowAnimation(
            led_strip=self,
            loop_limit=loop_limit,
            brightness=brightness,
            duration_ms=duration_ms,
            pause_ms=pause_ms
        ).glow()

    def beats(self,
              rgb_colors=None,
              brightness=1,
              brightness_fixed=False,
              max_height=1,
              loop_limit=None,
              duration_ms=200,
              pause_ms=300,
              direction='up',
              num_random_colors=5):
        BeatsUpAndDown(
            led_strip=self,
            rgb_colors=rgb_colors,
            brightness=brightness,
            brightness_fixed=brightness_fixed,
            max_height=max_height,
            loop_limit=loop_limit,
            duration_ms=duration_ms,
            pause_ms=pause_ms,
            direction=direction,
            num_random_colors=num_random_colors
        ).glow()

    def moving_dot(self,
                   rgb_colors=None,
                   brightness=1,
                   loop_limit=None,
                   duration_ms=200,
                   pause_a_ms=0,
                   pause_b_ms=300,
                   direction='up',
                   num_random_colors=5):
        MovingDot(
            led_strip=self,
            rgb_colors=rgb_colors,
            brightness=brightness,
            loop_limit=loop_limit,
            duration_ms=duration_ms,
            pause_a_ms=pause_a_ms,
            pause_b_ms=pause_b_ms,
            direction=direction,
            num_random_colors=num_random_colors
        ).glow()

    def light_up(self,
                 rgb_colors=None,
                 brightness=1,
                 loop_limit=None,
                 duration_ms=200,
                 pause_ms=200,
                 num_random_colors=5,
                 sections='all'):
        LightUp(
            led_strip=self,
            rgb_colors=rgb_colors,
            brightness=brightness,
            loop_limit=loop_limit,
            duration_ms=duration_ms,
            pause_ms=pause_ms,
            num_random_colors=num_random_colors,
            sections=sections
        ).glow()

    def transition(self,
                   rgb_colors=None,
                   brightness=1,
                   loop_limit=None,
                   duration_ms=200,
                   pause_ms=200,
                   num_random_colors=5,
                   sections='all'):
        Transition(
            led_strip=self,
            rgb_colors=rgb_colors,
            brightness=brightness,
            loop_limit=loop_limit,
            duration_ms=duration_ms,
            pause_ms=pause_ms,
            num_random_colors=num_random_colors,
            sections=sections
        ).glow()
