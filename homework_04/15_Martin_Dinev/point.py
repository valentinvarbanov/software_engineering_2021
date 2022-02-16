"""
This file is will show us the relative position of two circles and
is a part of out homework for Software engineering
"""

# pylint: disable=R0903

import enum
from math import sqrt, pow as power

class RelativePosition(enum.Enum):
    """
    Enum for the ways how one circle can be to another one
    """
    NO_COMMON_POINTS = -1
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 0

class Point():
    """
    Class that defines point with two coordinates
    """
    def __init__(self, x_coordinate, y_coordinate) -> None:
        assert isinstance(x_coordinate, float)
        assert isinstance(y_coordinate, float)

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

class Circle():
    """
    Class that defines a circle
    """
    def __init__(self, center, radius) -> None:
        assert isinstance(center, Point)
        assert isinstance(radius, float)

        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        """
        Function that finds where is one circle to another
        according to their radius and center.
        """
        assert isinstance(circle, Circle)
        if circle.center.x_coordinate == self.center.x_coordinate and \
            circle.center.y_coordinate == self.center.y_coordinate:
            return RelativePosition.SAME

        distance = sqrt(power(circle.center.x_coordinate - self.center.x_coordinate, 2) + \
            power(circle.center.y_coordinate - self.center.y_coordinate, 2))
        if distance > self.radius + circle.radius:
            return RelativePosition.NO_COMMON_POINTS

        if abs(distance - (self.radius + circle.radius)) < 0.0001:
            return RelativePosition.TOUCHING

        #distance < self.radius + circle.radius:
        if distance + circle.radius < self.radius or \
            (distance + circle.radius) - self.radius < 0.0001:
            return RelativePosition.SAME

        return RelativePosition.INTERSECTING

circle1 = Circle(Point(0.0, 0.0), 10.0)
circle2 = Circle(Point(4.0, 0.0), 6.0)
print(circle1.find_relative_position(circle2))
