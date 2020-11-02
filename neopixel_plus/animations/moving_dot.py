import time

from neopixel_plus.helper import Color, RunningAnimation


class MovingDot:
    def __init__(self,
                 led_strip,
                 loop_limit=None,
                 duration_ms=200,
                 pause_a_ms=0,
                 pause_b_ms=300,
                 start='start',
                 rgb_colors=None,
                 brightness=1,
                 stop_ongoing_animation=False,
                 num_random_colors=5):
        self.led_strip = led_strip
        self.stop_ongoing_animation = stop_ongoing_animation,
        self.loop_limit = loop_limit
        self.loops = 0
        self.duration_ms = duration_ms
        self.pause_a_ms = pause_a_ms
        self.pause_b_ms = pause_b_ms
        self.start = start
        self.selector = {
            "start": [-1, -2, -3, -4, -5],
            "end": [0, 1, 2, 3, 4]
        }

        self.colors = Color(
            rgb_colors=rgb_colors,
            brightness=brightness,
            num_random_colors=num_random_colors
        )

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.strip_length)/1000

    def create_dot(self):
        if self.led_strip.debug:
            print('MovingDot().create_dot()')

        self.dot = [self.colors.black]*5

        counter = 0
        for selected in self.selector[self.start]:
            self.colors.brightness = (
                1-(counter*0.225)) * self.colors.brightness_max
            self.colors.correct()
            self.dot[selected] = self.colors.selected
            counter += 1

    def change_direction(self):
        if self.led_strip.debug:
            print('MovingDot().change_direction()')

        if self.start == 'start':
            self.start = 'end'
        else:
            self.start = 'start'

    def move_dot(self):
        if self.led_strip.debug:
            print('MovingDot().move_dot()')

        # move dot into view
        for selected in self.selector[self.start]:
            if self.start == 'start':
                self.led_strip.insert_led(0, self.dot[selected])
            else:
                self.led_strip.append_led(self.dot[selected])
            self.led_strip.write(s_after_wait=self.write_wait_time)

        # add black led to front and remove last led, to move dot
        while True:
            if self.start == 'start':
                self.led_strip.insert_led()
            else:
                self.led_strip.append_led()
            self.led_strip.write(s_after_wait=self.write_wait_time)

            # if all leds black, exit loop
            for led in self.led_strip.leds:
                if led[0] != 0 or led[1] != 0 or led[2] != 0:
                    break
            else:
                break

    def glow(self):
        if self.led_strip.debug:
            print('MovingDot().glow()')

        print('Moving dot:')
        try:
            # make sure leds are off
            self.led_strip.off()

            while True:
                # check if animation should be stopped or not
                if self.stop_ongoing_animation == True and RunningAnimation.check_animation_running() == False:
                    break

                # make sure duration is correct
                # create dot with tail
                self.create_dot()

                # move dot with tail and write
                self.move_dot()

                # once dot disappeared at the end: pause_a
                time.sleep(self.pause_a_ms/1000)

                # create new dot with tail and move in opposit start
                self.change_direction()
                self.create_dot()
                self.move_dot()
                self.change_direction()

                # once dot disappeared at the end: pause_b
                time.sleep(self.pause_b_ms/1000)

                # change to next color
                self.colors.next()

                self.loops += 1
                if self.loop_limit and self.loop_limit == self.loops:
                    print()
                    break

        except KeyboardInterrupt:
            import sys
            print()
            sys.exit(0)
