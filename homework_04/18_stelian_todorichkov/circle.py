"""
This file find the position of one circle
relative to other
"""
from enum import Enum
from math import sqrt

class RealativePosition(Enum):
    """
    Enum for all case of position
    """
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3

class Point:
    """
    Class for point with x and y
    """
    def __init__(self, x_cord, y_cord):
        assert isinstance(x_cord, float)
        assert isinstance(y_cord, float)
        self.x_cord = x_cord
        self.y_cord = y_cord

    def __eq__(self, other):
        assert isinstance(other, Point)
        return self.x_cord == other.x_cord and self.y_cord == other.y_cord

    def distane_between_points(self, other):
        """
        Function find distance between 2 points
        """
        assert isinstance(other, Point)
        sub_x = self.x_cord - other.x_cord
        sub_y = self.y_cord - other.y_cord
        return sqrt(sub_x ** 2 + sub_y ** 2)

class Circle:
    """
    Class for circle with center and radius
    """
    def __init__(self, ceter, radius):
        assert isinstance(ceter, Point)
        assert isinstance(radius, float)
        assert radius > 0

        self.center = ceter
        self.radius = radius

    def __eq__(self, other):
        assert isinstance(other, Circle)
        return self.center == other.center and self.radius == other.radius

    def find_relative_position(self, other):
        """
        Function find relative position of 2 circles
        """
        assert isinstance(other, Circle)
        distance = self.center.distane_between_points(other.center)
        if self == other:
            return RealativePosition.SAME
        if abs(self.radius - other.radius) < distance < (self.radius + other.radius):
            return RealativePosition.INTERSECTING
        if distance == (self.radius + other.radius) \
                or distance == abs(self.radius - other.radius):
            return RealativePosition.TOUCHING
        return RealativePosition.NO_COMMON_POINTS
