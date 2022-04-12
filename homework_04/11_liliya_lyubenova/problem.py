"""
Find relative position for 2 circles
"""
import enum
from math import sqrt

class RelativePosition(enum.Enum):
    """
    Relative position enums
    """
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

# pylint: disable=R0903
class Point():
    """
    Point class
    """
    def __init__(self, _x_, _y_):
        self.x__ = float(_x_)
        self.y__ = float(_y_)

    @staticmethod
    def distance_between_two_centers(center_1, center_2):
        """
        Distance between two centers method
        """
        return sqrt(pow((center_1.x__ - center_2.x__), 2) + pow((center_1.y__ - center_2.y__), 2))
class Circle:
    """
    Circle class
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)
        assert radius > 0

    def find_relative_position(self, circle_2):
        """
        Find relative position method
        """
        distance = Point.distance_between_two_centers(self.center, circle_2.center)
        sum_radiuses = self.radius + circle_2.radius
        sub_radiuses = abs(self.radius - circle_2.radius)

        if distance > sum_radiuses:
            return RelativePosition.NO_COMMON_POINTS
        if distance == sum_radiuses:
            return RelativePosition.TOUCHING
        if sub_radiuses < distance < sum_radiuses:
            return RelativePosition.INTERSECTING
        if distance <= sub_radiuses or self.center == circle_2.center:
            return RelativePosition.SAME
        return None
