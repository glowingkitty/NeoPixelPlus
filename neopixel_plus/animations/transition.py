import time

from neopixel_plus.helper import Color, RunningAnimation


class Transition:
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

        self.transition_steps = 20
        self.write_wait_time = (self.duration_ms/self.transition_steps)/1000

        self.selected_leds = self.led_strip.get_led_selectors(
            self.sections)

    def glow(self):
        if self.led_strip.debug:
            print('Transition().glow()')

        print('Transition:')
        try:
            # make sure leds are off
            self.led_strip.off()

            while True:
                # check if animation should be stopped or not
                if self.stop_ongoing_animation == True and RunningAnimation.check_animation_running() == False:
                    break

                # add or substract difference between rgb values and update color - to make transition

                steps_counter = 0
                target_color = self.colors.selected
                difference = [
                    target_color[0] -
                    self.led_strip.leds[self.selected_leds[0]][0],
                    target_color[1] -
                    self.led_strip.leds[self.selected_leds[0]][1],
                    target_color[2] -
                    self.led_strip.leds[self.selected_leds[0]][2],
                ]

                difference_per_step = [
                    round(difference[0]/self.transition_steps),
                    round(difference[1]/self.transition_steps),
                    round(difference[2]/self.transition_steps),
                ]

                while steps_counter != self.transition_steps:

                    self.colors.selected = [
                        self.led_strip.leds[self.selected_leds[0]
                                            ][0]+difference_per_step[0],
                        self.led_strip.leds[self.selected_leds[0]
                                            ][1]+difference_per_step[1],
                        self.led_strip.leds[self.selected_leds[0]
                                            ][2]+difference_per_step[2],
                    ]

                    # make to not select invalid RGB values
                    new_list = []
                    for number in self.colors.selected:
                        if number < 0:
                            new_list.append(0)
                        elif number > 255:
                            new_list.append(255)
                        else:
                            new_list.append(number)
                    self.colors.selected = new_list

                    for i in self.selected_leds:
                        self.led_strip.leds[i] = self.colors.selected
                    self.led_strip.write(s_after_wait=self.write_wait_time)

                    steps_counter += 1

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
