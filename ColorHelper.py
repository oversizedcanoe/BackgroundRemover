class ColorHelper:
    def __init__(self, wiggle_room):
        self.wiggle_room = wiggle_room
        self.min_red = None
        self.max_red = None
        self.min_blue = None
        self.max_blue = None
        self.min_green = None
        self.max_green = None

    def __mins_and_maxes_initialized(self):
        return (self.min_red is None \
                or self.max_red is None \
                or self.min_green is None \
                or self.max_green is None \
                or self.min_blue is None \
                or self.max_blue is None)

    def __initialize_mins_and_maxes(self, bg_color):
        self.min_red = self.__get_min_color_value(bg_color[0])
        self.max_red = self.__get_max_color_value(bg_color[0])
        self.min_green = self.__get_min_color_value(bg_color[1])
        self.max_green = self.__get_max_color_value(bg_color[1])
        self.min_blue = self.__get_min_color_value(bg_color[2])
        self.max_blue = self.__get_max_color_value(bg_color[2])

    def __get_min_color_value(self, color_value):
        min_value = round(color_value * (1 - self.wiggle_room))

        if min_value < 0:
            min_value = 0

        return min_value

    def __get_max_color_value(self, color_value):
        max_value = round((color_value * (1 + self.wiggle_room)) + 1)

        if max_value >= 255:
            max_value = 256

        return max_value

    def is_close_to_background(self, color, background_color) -> bool:
        bg_r_value = background_color[0]
        bg_g_value = background_color[1]
        bg_b_value = background_color[2]

        if color == (bg_r_value, bg_g_value, bg_b_value):
            return True

        if self.__mins_and_maxes_initialized():
            self.__initialize_mins_and_maxes(background_color)

        red_in_range = color[0] in range(self.min_red, self.max_red)
        green_in_range = color[1] in range(self.min_green, self.max_green)
        blue_in_range = color[2] in range(self.min_blue, self.max_blue)

        return red_in_range and green_in_range and blue_in_range
