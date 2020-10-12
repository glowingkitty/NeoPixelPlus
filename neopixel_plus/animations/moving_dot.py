import time

from neopixel_plus.helper import Color


class MovingDot:
    def __init__(self,
                 led_strip,
                 loop_limit=None,
                 duration_ms=200,
                 pause_a_ms=0,
                 pause_b_ms=300,
                 direction='up',
                 rgb_colors=None,
                 brightness=1,
                 num_random_colors=5):
        self.led_strip = led_strip
        self.loop_limit = loop_limit
        self.duration_ms = duration_ms
        self.pause_a_ms = pause_a_ms
        self.pause_b_ms = pause_b_ms
        self.direction = direction
        self.selector = {
            "up": [-1, -2, -3, -4, -5],
            "down": [0, 1, 2, 3, 4]
        }

        self.colors = Color(
            rgb_colors=rgb_colors,
            brightness=brightness,
            num_random_colors=num_random_colors
        )

        self.write_wait_time = (
            self.duration_ms/2/self.led_strip.strip_length)/1000

    def create_dot(self):
        self.dot = [self.colors.black]*5

        counter = 0
        for selected in self.selector[self.direction]:
            self.colors.brightness = (
                1-(counter*0.225)) * self.colors.brightness_max
            self.colors.correct()
            self.dot[selected] = self.colors.selected
            counter += 1

    def change_direction(self):
        if self.direction == 'up':
            self.direction = 'down'
        else:
            self.direction = 'up'

    def move_dot(self):
        # move dot into view
        for selected in self.selector[self.direction]:
            if self.direction == 'up':
                self.led_strip.leds.insert(0, self.dot[selected])
                self.led_strip.leds = self.led_strip.leds[:-1]
            else:
                self.led_strip.leds.append(self.dot[selected])
                self.led_strip.leds = self.led_strip.leds[1:]
            self.led_strip.write(s_after_wait=self.write_wait_time)

        # add black led to front and remove last led, to move dot
        while True:
            if self.direction == 'up':
                self.led_strip.leds.insert(0, self.colors.black)
                self.led_strip.leds = self.led_strip.leds[:-1]
            else:
                self.led_strip.leds.append(self.colors.black)
                self.led_strip.leds = self.led_strip.leds[1:]
            self.led_strip.write(s_after_wait=self.write_wait_time)

            # if all leds black, exit loop
            for led in self.led_strip.leds:
                if led != self.colors.black:
                    break
            else:
                break

    def glow(self):
        print('Moving dot:')
        try:
            # make sure leds are off
            self.led_strip.off()

            while True:
                # make sure duration is correct
                # create dot with tail
                self.create_dot()

                # move dot with tail and write
                self.move_dot()

                # once dot disappeared at the end: pause_a
                time.sleep(self.pause_a_ms/1000)

                # create new dot with tail and move in opposit direction
                self.change_direction()
                self.create_dot()
                self.move_dot()
                self.change_direction()

                # once dot disappeared at the end: pause_b
                time.sleep(self.pause_b_ms/1000)

                # change to next color
                self.colors.next()

        except KeyboardInterrupt:
            import sys
            print()
            sys.exit(0)
