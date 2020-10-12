import time

from neopixel_plus.helper import Color


class BeatsUpAndDown:
    def __init__(self,
                 led_strip,
                 loop_limit=None,
                 duration_ms=200,
                 pause_ms=300,
                 direction='up',
                 rgb_colors=None,
                 brightness=1,
                 brightness_fixed=False,
                 max_height=1,
                 num_random_colors=5
                 ):
        self.led_strip = led_strip
        self.loop_limit = loop_limit
        self.duration_ms = duration_ms
        self.pause_ms = pause_ms
        self.direction = direction
        self.max_height = max_height
        self.led_strip.addressable_strip_length = round(
            self.led_strip.strip_length*self.max_height)

        self.colors = Color(
            rgb_colors=rgb_colors,
            brightness=brightness,
            brightness_fixed=brightness_fixed,
            num_random_colors=num_random_colors
        )

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.addressable_strip_length)/1000

    def glow(self):
        print('Beats up and down:')
        try:
            loops = 0

            # make sure leds are off
            self.led_strip.off()

            while True:
                # update color if brightness different
                if self.colors.brightness != 1 and self.colors.brightness_fixed:
                    self.colors.correct()

                # color LEDs
                for i in range(self.led_strip.addressable_strip_length):
                    # if brightness_fixed==False: set brightness depending on what led is glowing up
                    if self.colors.brightness_fixed == False:
                        # led 1: 30% of self.brightness_max
                        # led 2: 30% of max + (i * 70%/self.led_strip.strip_length)
                        # last LED: 100% * self.brightness_max
                        self.colors.brightness = round((0.3*self.colors.brightness_max) +
                                                       ((i+1)*(0.7/self.led_strip.addressable_strip_length)), 2)
                        self.colors.correct()

                    if self.direction == 'down':
                        i = - (i+1)

                    i = self.led_strip.get_led(i, self.direction)
                    self.led_strip.leds[i] = self.colors.selected

                    self.led_strip.write(s_after_wait=self.write_wait_time)

                # then make them black
                for i in range(self.led_strip.addressable_strip_length):
                    if self.direction == 'up':
                        i = -(i+1)
                    i = self.led_strip.get_led(i, self.direction)
                    self.led_strip.leds[i] = self.colors.black

                    self.led_strip.write(s_after_wait=self.write_wait_time)

                # change to next color
                self.colors.next()

                if self.pause_ms:
                    time.sleep(self.pause_ms/1000)

                loops += 1

                if self.loop_limit and self.loop_limit == loops:
                    break
        except KeyboardInterrupt:
            import sys
            print()
            sys.exit(0)
