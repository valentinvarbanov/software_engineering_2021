# pylint: disable=R0903
"""
Imports
"""
from enum import Enum
import math

class RelativePosition(Enum):
    """
    Enum Relative Position
    """
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

def find_distance(point_one, point_two):
    """
    Calculate the distance between two points
    """
    assert isinstance(point_one, Point)
    assert isinstance(point_two, Point)

    return math.sqrt(pow(point_two.coordinate_x - point_one.coordinate_x, 2)\
         + pow(point_two.coordinate_y - point_one.coordinate_y, 2))

class Point:
    """
    Class for Point
    """
    def __init__(self, coordinate_x, coordinate_y):
        assert isinstance(coordinate_x, float)
        assert isinstance(coordinate_y, float)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

class Circle:
    """
    Class for circle
    """
    def __init__(self, center, radius):
        assert isinstance(center, Point)
        assert isinstance(radius, float)
        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        """
        Function that finds position of circle1 to circle2
        by given circle radius and center
        """
        assert isinstance(circle, Circle)
        if circle.center.coordinate_x == self.center.coordinate_x and \
            circle.center.coordinate_y == self.center.coordinate_y:
            return RelativePosition.SAME

        distance = find_distance(self.center, circle.center)
        if distance > self.radius + circle.radius:
            return RelativePosition.NO_COMMON_POINTS
        if abs(distance - (self.radius + circle.radius)) < 0.0001:
            return RelativePosition.TOUCHING
        if distance + circle.radius < self.radius or \
            (distance + circle.radius) - self.radius < 0.0001:
            return RelativePosition.SAME

        return RelativePosition.INTERSECTING
    