"""A module that contains a basic point class"""
from math import sqrt

class Point:
    """A simple class that defines a point"""

    def __init__(self, input_x, input_y):
        self.set_x(input_x)
        self.set_y(input_y)

    def get_x(self):
        """A getter method for the x coordinate field"""
        return self.__x

    def get_y(self):
        """A getter method for the y coordinate field"""
        return self.__y

    def set_x(self, new_x):
        """A setter method for the x coordinate field"""
        if isinstance(new_x, float) is not True:
            raise ValueError("X should be of type float")
        self.__x = new_x

    def set_y(self, new_y):
        """A setter method for the y coordinate field"""
        if isinstance(new_y, float) is not True:
            raise ValueError("Y should be of type float")
        self.__y = new_y

    @staticmethod
    def get_distance_between_two_points(point_a, point_b):
        """A static method that returns the distance between two points"""
        return sqrt(pow((point_a.get_x() - point_b.get_x()), 2) + \
            pow((point_a.get_y() - point_b.get_y()), 2))
