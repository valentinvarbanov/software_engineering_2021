"""
This file finds the relative position of two circles
"""

# pylint: disable=R0903
from enum import Enum
from math import sqrt

class RelativePosition(Enum):
    """
    Enum for the types of relation between circles
    """
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

class Point:
    """
    Class that defines a point
    """
    def __init__(self, x_coord, y_coord):
        assert isinstance(x_coord, float) and isinstance(y_coord, float)
        self.x_coord = x_coord
        self.y_coord = y_coord


class Circle:
    """
    Class that defines a circle
    """
    def __init__(self, center, radius):
        assert isinstance(center, Point) and isinstance(radius, float)
        self.center = center
        self.radius = radius

    def find_relative_position(self, other_circle):
        """
        Function that finds relative postion of one circle to another
        """
        assert isinstance(other_circle, Circle)

        centers_distance = sqrt((self.center.x_coord - other_circle.center.x_coord)**2
                + (self.center.y_coord - other_circle.center.y_coord)**2)

        if (self.center.x_coord == other_circle.center.x_coord
             and self.center.y_coord == other_circle.center.y_coord
             and self.radius == other_circle.radius):
            return RelativePosition.SAME
        if abs(self.radius - other_circle.radius) < centers_distance <  self.radius + other_circle.radius:
            return RelativePosition.INTERSECTING
        if centers_distance == self.radius + other_circle.radius \
                         or centers_distance == (abs(self.radius - other_circle.radius)):
            return RelativePosition.TOUCHING

        return RelativePosition.NO_COMMON_POINTS
