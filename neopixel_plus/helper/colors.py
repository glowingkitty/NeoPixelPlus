import random


class Color:
    def __init__(self, rgb_colors, brightness=1, brightness_fixed=False, num_random_colors=5):
        self.rgb_colors = rgb_colors if rgb_colors else self.random_set(
            num_random_colors)
        self.selected_num = 0
        self.selected_max = len(self.rgb_colors)-1
        self.base_color = self.rgb_colors[self.selected_num]
        self.brightness = brightness
        self.brightness_max = brightness
        self.brightness_fixed = brightness_fixed

        self.correct()

    @property
    def black(self):
        return [0, 0, 0]

    @property
    def white(self):
        return [255, 255, 255]

    def random(self):
        return [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    def random_set(self, how_many):
        array = [0]*how_many
        return [self.random() for x in array]

    def correct(self):
        r = int(self.base_color[0] * self.brightness)
        g = int(self.base_color[1] * self.brightness)
        b = int(self.base_color[2] * self.brightness)

        self.selected = [r if r < 255 else 255, g if g <
                         255 else 255, b if b < 255 else 255]

    def next(self):
        # select next color from self.rgb_colors, with correct brightness
        if self.selected_num == self.selected_max:
            self.selected_num = 0
        else:
            self.selected_num += 1
        self.base_color = self.rgb_colors[self.selected_num]
        self.correct()
