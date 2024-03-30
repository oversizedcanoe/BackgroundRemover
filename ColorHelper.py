import math

class ColorHelper:
    MAX_COLOR_DIFFERENCE = 764.83
    MIN_WIGGLE_ROOM = 0.03

    def __init__(self, background_color):
        self.__wiggle_room = self.MIN_WIGGLE_ROOM
        self.background_color = background_color
        self.min_red = None
        self.max_red = None
        self.min_blue = None
        self.max_blue = None
        self.min_green = None
        self.max_green = None

    def __mins_and_maxes_not_initialized(self):
        return (self.min_red is None \
                or self.max_red is None \
                or self.min_green is None \
                or self.max_green is None \
                or self.min_blue is None \
                or self.max_blue is None)

    def __initialize_mins_and_maxes(self):
        self.min_red = self.__get_min_color_value(self.background_color[0])
        self.max_red = self.__get_max_color_value(self.background_color[0])
        self.min_green = self.__get_min_color_value(self.background_color[1])
        self.max_green = self.__get_max_color_value(self.background_color[1])
        self.min_blue = self.__get_min_color_value(self.background_color[2])
        self.max_blue = self.__get_max_color_value(self.background_color[2])

    def __get_min_color_value(self, color_value):
        min_value = round(color_value * (1 - self.__wiggle_room))

        if min_value < 0:
            min_value = 0

        return min_value

    def __get_max_color_value(self, color_value):
        max_value = round((color_value * (1 + self.__wiggle_room)) + 1)

        if max_value >= 255:
            max_value = 256

        return max_value
    
    def get_wiggle_room(self):
        return self.__wiggle_room
    
    def set_wiggle_room(self, wiggle_room_value):
        self.__wiggle_room = wiggle_room_value
        self.__initialize_mins_and_maxes()

    def is_close_to_background(self, color, background_color) -> bool:
        bg_r_value = background_color[0]
        bg_g_value = background_color[1]
        bg_b_value = background_color[2]

        if color == (bg_r_value, bg_g_value, bg_b_value):
            return True

        if self.__mins_and_maxes_not_initialized():
            self.__initialize_mins_and_maxes()

        red_in_range = color[0] in range(self.min_red, self.max_red)
        green_in_range = color[1] in range(self.min_green, self.max_green)
        blue_in_range = color[2] in range(self.min_blue, self.max_blue)

        return red_in_range and green_in_range and blue_in_range

    def get_color_difference(self, average_color, background_color):
        # Euclidean distance
        delta_r_squared = (average_color[0] - background_color[0]) ** 2
        delta_g_squared = (average_color[1] - background_color[1]) ** 2
        delta_b_squared = (average_color[2] - background_color[2]) ** 2
        average_r = round((average_color[0] + background_color[0]) / 2)

        # redmean -> https://en.wikipedia.org/wiki/Color_difference
        term_1 = (2 + (average_r / 256)) * delta_r_squared
        term_2 = 4 * delta_g_squared
        term_3 = (2 + ((255 - average_r) / 256)) * delta_b_squared

        return math.sqrt(term_1 + term_2 + term_3)
            
    def update_ideal_wiggle_room(self, color_difference):
        # In "redmean" Euclidean distance, the largest value (where the background is white
        # and all non-background is black) is 764.83.
        # The lowest observable value would be ~40(?), but 0 is the actual lowest.

        # I find squaring them before dividing gets a more accurate result
        color_difference_percentage = color_difference**2 / self.MAX_COLOR_DIFFERENCE**2
        self.set_wiggle_room(color_difference_percentage)
        print(f'ideal wiggle room: {self.__wiggle_room}')
