import time

from neopixel_plus.helper import Color, RunningAnimation


class BeatsUpAndDown:
    def __init__(self,
                 led_strip,
                 loop_limit=None,
                 duration_ms=200,
                 pause_ms=300,
                 start='start',
                 rgb_colors=None,
                 brightness=1,
                 brightness_fixed=False,
                 max_height=1,
                 num_random_colors=5,
                 stop_ongoing_animation=False,
                 ):
        self.led_strip = led_strip
        self.stop_ongoing_animation = stop_ongoing_animation,
        self.loop_limit = loop_limit
        self.loops = 0
        self.duration_ms = duration_ms
        self.pause_ms = pause_ms
        self.start = start
        self.max_height = max_height

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.addressable_strip_length)/1000

        self.colors = Color(
            rgb_colors=rgb_colors,
            brightness=brightness,
            brightness_fixed=brightness_fixed,
            num_random_colors=num_random_colors
        )

        if self.start == 'start' or self.start == 'end':
            self.led_strip.addressable_strip_length = round(
                self.led_strip.strip_length*self.max_height)
            self.selected_leds = range(self.led_strip.addressable_strip_length)
            self.selected_leds_counter_up = self.led_strip.addressable_strip_length
            self.selected_leds_counter_down = round(self.led_strip.addressable_strip_length -
                                                    self.selected_leds_counter_up)
        else:
            self.led_strip.addressable_strip_length = self.led_strip.strip_length
            self.selected_leds = range(
                round(self.led_strip.addressable_strip_length/2))
            self.selected_leds_counter_up = round(self.max_height *
                                                  round(self.led_strip.addressable_strip_length/2))
            self.selected_leds_counter_down = round(round(
                self.led_strip.addressable_strip_length/2)-self.selected_leds_counter_up)

    def color_leds(self):
        if self.led_strip.debug:
            print('BeatsUpAndDown().color_leds()')

        # color LEDs
        for i in self.selected_leds[:self.selected_leds_counter_up]:
            # if brightness_fixed==False: set brightness depending on what led is glowing up
            if self.colors.brightness_fixed == False:
                # led 1: 30% of self.brightness_max
                # led 2: 30% of max + (i * 70%/self.led_strip.strip_length)
                # last LED: 100% * self.brightness_max
                if self.start == 'start + end' or self.start == 'center':
                    self.colors.brightness = round((0.3*self.colors.brightness_max) +
                                                   ((i+1)*(0.7/((self.led_strip.addressable_strip_length*self.max_height)/2))), 2)
                else:
                    self.colors.brightness = round((0.3*self.colors.brightness_max) +
                                                   ((i+1)*(0.7/self.led_strip.addressable_strip_length)), 2)
                self.colors.correct()

            # "start" option "start & end" and "center"
            if self.start == 'end':
                i = [-(i+1)]
            elif self.start == 'start':
                i = [i]
            elif self.start == 'start + end':
                i = [i, -(i+1)]
            elif self.start == 'center':
                i = [i+round(self.led_strip.addressable_strip_length/2), -
                     (i+1)+round(self.led_strip.addressable_strip_length/2)]

            for led in i:
                led = self.led_strip.get_led(led, self.start)
                self.led_strip.leds[led] = self.colors.selected

            self.led_strip.write(s_after_wait=self.write_wait_time)

    def make_leds_black(self):
        if self.led_strip.debug:
            print('BeatsUpAndDown().make_leds_black()')

        # then make them black
        for i in self.selected_leds[self.selected_leds_counter_down:]:
            if self.start == 'start':
                i = [-(i+1)]
            elif self.start == 'end':
                i = [i]
            elif self.start == 'start + end':
                i = [-(i+1)+round(self.led_strip.addressable_strip_length/2),
                     i+round(self.led_strip.addressable_strip_length/2)]
            elif self.start == 'center':
                i = [i, -(i+1)]

            for led in i:
                led = self.led_strip.get_led(led, self.start)
                self.led_strip.leds[led] = self.colors.black

            self.led_strip.write(s_after_wait=self.write_wait_time)

    def glow(self):
        if self.led_strip.debug:
            print('BeatsUpAndDown().glow()')

        print('Beats up and down:')
        try:
            # make sure leds are off
            self.led_strip.off()

            while True:
                # check if animation should be stopped or not
                if self.stop_ongoing_animation == True and RunningAnimation.check_animation_running() == False:
                    break

                # update color if brightness different
                if self.colors.brightness != 1 and self.colors.brightness_fixed:
                    self.colors.correct()

                self.color_leds()
                self.make_leds_black()

                # change to next color
                self.colors.next()

                if self.pause_ms:
                    time.sleep(self.pause_ms/1000)

                self.loops += 1
                if self.loop_limit and self.loop_limit == self.loops:
                    print()
                    break
        except KeyboardInterrupt:
            import sys
            print()
            sys.exit(0)
