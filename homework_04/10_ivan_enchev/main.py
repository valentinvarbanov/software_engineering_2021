"""Task Logic"""

from enum import Enum
from math import fabs, sqrt


# pylint: disable=R0903

def find_distance(point_a, point_b):
    """Find distance between two points."""

    side_a = fabs(point_a.x_coord - point_b.x_coord)
    side_b = fabs(point_a.y_coord - point_b.y_coord)
    return sqrt((side_b * side_b) + (side_a * side_a))


class RelativePosition(Enum):
    """Relative points, part of the task"""
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4


class Point:
    """A class for a point in a cartesian coordinate system"""
    def __init__(self, x_coord, y_coord) -> None:
        assert isinstance(x_coord, float)
        assert isinstance(y_coord, float)
        self.x_coord = x_coord
        self.y_coord = y_coord


class Circle:
    """A class for a circle in a cartesian coordinate system"""
    def __init__(self, center, radius) -> None:
        assert isinstance(center, Point)
        assert isinstance(radius, float)
        self.center = center
        self.radius = radius

    def find_relative_position(self, another):
        """Find the position of one circle erlative to another one."""
        assert isinstance(another, Circle)

        line = find_distance(self.center, another.center)
        position = RelativePosition.SAME

        if line > (self.radius + another.radius):
            position = RelativePosition.NO_COMMON_POINTS

        elif line == (self.radius + another.radius) or (line == fabs((self.radius - another.radius)) and line != 0):
            position = RelativePosition.TOUCHING

        elif (self.radius + another.radius) > line > fabs((self.radius - another.radius)):
            position = RelativePosition.INTERSECTING

        return position

