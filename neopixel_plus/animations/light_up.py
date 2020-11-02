import time

from neopixel_plus.helper import Color, RunningAnimation


class LightUp:
    def __init__(self,
                 led_strip,
                 rgb_colors=None,
                 brightness=1,
                 loop_limit=None,
                 duration_ms=200,
                 pause_ms=200,
                 num_random_colors=5,
                 stop_ongoing_animation=False,
                 sections='all'):
        self.led_strip = led_strip
        self.stop_ongoing_animation = stop_ongoing_animation,
        self.loop_limit = loop_limit
        self.loops = 0
        self.duration_ms = duration_ms
        self.pause_ms = pause_ms
        self.sections = sections
        self.colors = Color(
            rgb_colors=rgb_colors,
            brightness=brightness,
            num_random_colors=num_random_colors
        )

        self.write_wait_time = (
            self.duration_ms/((round(self.colors.brightness_max, 1)/0.1)*2)/1000)

    def glow(self):
        print('Light up:')
        try:
            # make sure leds are off
            self.led_strip.off()

            while True:
                # check if animation should be stopped or not
                if self.stop_ongoing_animation == True and RunningAnimation.check_animation_running() == False:
                    break

                # go over levels of brightness from 0 to 1 and
                self.colors.brightness = 0
                self.colors.correct()

                self.selected_leds = self.led_strip.get_led_selectors(
                    self.sections)

                # light up
                while self.colors.brightness != round(self.colors.brightness_max, 1):
                    for i in self.selected_leds:
                        self.led_strip.leds[i] = self.colors.selected
                    self.led_strip.write(s_after_wait=self.write_wait_time)

                    self.colors.brightness = round(
                        self.colors.brightness+0.1, 1)
                    self.colors.correct()

                # light down
                while self.colors.brightness != 0.0:
                    self.colors.brightness = round(
                        self.colors.brightness-0.1, 1)
                    self.colors.correct()
                    for i in self.selected_leds:
                        self.led_strip.leds[i] = self.colors.selected
                    self.led_strip.write(s_after_wait=self.write_wait_time)

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
