import math
import time

# TODO add Color() and simplify code (create rainbow once, then move it)
from neopixel_plus.helper import RunningAnimation


class RainbowAnimation:
    def __init__(self,
                 led_strip,
                 brightness=1,
                 loop_limit=None,
                 duration_ms=1000,
                 stop_ongoing_animation=False,
                 pause_ms=None):
        self.led_strip = led_strip
        self.stop_ongoing_animation = stop_ongoing_animation,
        self.brightness_max = brightness
        self.loop_limit = loop_limit
        self.duration_ms = duration_ms
        self.pause_ms = pause_ms

        self.time_passed_ms = 0

    def set_time_passed_ms(self):
        if self.led_strip.debug:
            print('RainbowAnimation().set_time_passed_ms()')

        # if duration 1000 ms = 17 loops * 60ms
        # if duration 500 ms = 8.5 loops 120ms
        # if duration 250 ms = 4.25 loops 240ms
        # if duration 100 ms = 1.7 loops 600ms
        full_duration = 1000
        default_rate = 60

        added_ms = (full_duration/self.duration_ms)*default_rate

        self.time_passed_ms += added_ms

    def set_brightness(self, counter, max_counter):
        if self.led_strip.debug:
            print('RainbowAnimation().set_brightness(counter={},max_counter={})'.format(
                counter, max_counter))

        # if counter == 1 => brightness 0.3
        # if counter == 2 => brightness 0.6
        # if counter == max_counter-1 => brightness 0.3
        # if counter == max_counter-2 => brightness 0.6
        if self.duration_ms and self.pause_ms and counter == 0:
            self.brightness = 0.3*self.brightness_max
        elif self.duration_ms and self.pause_ms and counter == 1:
            self.brightness = 0.6*self.brightness_max
        elif self.duration_ms and self.pause_ms and counter == (max_counter-2):
            self.brightness = 0.6*self.brightness_max
        elif self.duration_ms and self.pause_ms and counter == (max_counter-1):
            self.brightness = 0.3*self.brightness_max
        else:
            self.brightness = 1*self.brightness_max

    def get_max_counter(self):
        if self.led_strip.debug:
            print('RainbowAnimation().get_max_counter()')

        # if duration 1000 ms = 17 loops * 60ms
        # if duration 500 ms = 8.5 loops 120ms
        # if duration 250 ms = 4.25 loops 240ms
        # if duration 100 ms = 1.7 loops 600ms
        full_duration = 1000
        loops = 17

        return round((self.duration_ms/full_duration)*loops)

    def glow(self):
        if self.led_strip.debug:
            print('RainbowAnimation().glow()')

        print('Rainbow:')
        try:
            # if duration, need to adapt time_passed to make one full color loop (and then pause if pause set)
            # turn LEDs rainbow
            counter = 0
            loops = 0
            max_counter = self.get_max_counter()
            while True:
                # check if animation should be stopped or not
                if self.stop_ongoing_animation == True and RunningAnimation.check_animation_running() == False:
                    break

                self.set_brightness(counter, max_counter)

                # turn LEDs black (off) for duration of pause
                if counter == max_counter:
                    if self.duration_ms and self.pause_ms:
                        self.led_strip.off()
                        time.sleep((self.pause_ms-10)/1000)

                    counter = 0
                    loops += 1

                    if self.loop_limit and self.loop_limit == loops:
                        print()
                        break

                else:

                    self.set_time_passed_ms()
                    for i in range(self.led_strip.strip_length):
                        i = self.led_strip.get_led(i)
                        color = self.rainbow_color(self.time_passed_ms, i,
                                                   self.brightness)
                        self.led_strip.leds[i] = color

                    self.led_strip.write()

                    counter += 1
        except KeyboardInterrupt:
            import sys
            print()
            sys.exit(0)

    def rainbow_color(self, t, i, brightness):
        if self.led_strip.debug:
            print('RainbowAnimation().rainbow_color(t={},i={},brightness={})'.format(
                t, i, brightness))

        t = t/1000
        a = (0.5, 0.5, 0.5)
        b = (0.5, 0.5, 0.5)
        c = (1.0, 1.0, 1.0)
        d = (0.00, 0.33, 0.67)

        k = t + 0.05 * i

        r = a[0] + b[0] * math.cos(6.28318 * (c[0] * k + d[0]))
        g = a[1] + b[1] * math.cos(6.28318 * (c[1] * k + d[1]))
        b = a[2] + b[2] * math.cos(6.28318 * (c[2] * k + d[2]))

        r = int(255.0 * r * brightness)
        g = int(255.0 * g * brightness)
        b = int(255.0 * b * brightness)

        return (r if r < 255 else 255, g if g < 255 else 255, b if b < 255 else 255)
