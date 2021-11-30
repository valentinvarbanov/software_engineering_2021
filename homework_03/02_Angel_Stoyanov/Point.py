from math import sqrt, pow

class Point:
    def __init__(self, input_x, input_y):
        self.set_x(input_x)
        self.set_y(input_y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def set_x(self, x):
        if isinstance(x, float) is not True:
            raise ValueError("X should be of type float")
        self.__x = x

    def set_y(self, y):
        if isinstance(y, float) is not True:
            raise ValueError("Y should be of type float")
        self.__y = y

    @staticmethod
    def get_distance_between_two_points(point_a, point_b):
        return sqrt(pow((point_a.x() - point_b.x()), 2) + pow((point_a.y() - point_b.y()), 2))
