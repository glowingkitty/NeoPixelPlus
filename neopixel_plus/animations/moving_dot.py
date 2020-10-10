import random


class MovingDot:
    def __init__(self,
                 led_strip,
                 color=None,
                 brightness=1,
                 brightness_fixed=False,
                 loop_limit=None,
                 duration_ms=200,
                 pause_a_ms=0,
                 pause_b_ms=300,
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

    def create_dot(self):
        self.color = self.base_color
        self.dot = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        counter = 0
        for selected in self.selector[self.direction]:
            self.brightness = (1-(counter*0.225)) * self.brightness_max
            self.set_color_brightness()
            self.dot[selected] = self.color
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
                self.led_strip.leds.insert(0, [0, 0, 0])
                self.led_strip.leds = self.led_strip.leds[:-1]
            else:
                self.led_strip.leds.append([0, 0, 0])
                self.led_strip.leds = self.led_strip.leds[1:]
            self.led_strip.write(s_after_wait=self.write_wait_time)

            # if all leds black, exit loop
            for led in self.led_strip.leds:
                if led != [0, 0, 0]:
                    break
            else:
                break

    def glow(self):
        # make sure leds are off
        self.led_strip.off()

        while True:
            # create dot with tail
            self.create_dot()

            # move dot with tail and write
            self.move_dot()

            # TODO once dot disappeared at the end: pause_a

            # create new dot with tail and move in opposit direction
            self.change_direction()
            self.create_dot()
            self.move_dot()
            self.change_direction()

            # TODO once dot disappeared at the end: pause_b

            # change color if color supposed to be random
            if self.change_color_random:
                self.base_color = self.get_random_color()
