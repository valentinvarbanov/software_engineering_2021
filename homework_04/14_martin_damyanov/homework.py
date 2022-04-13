"""Homework for circles"""
from enum import Enum #imports enum class
import math #imports math functions

class RelativePosition(Enum):
    """enumerates the four possible cases"""
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

def distance(a_point, b_point):
    """Returns the distance between two given points"""
    assert isinstance(a_point, Point)
    assert isinstance(b_point, Point)
    return math.sqrt(pow(b_point.x_coord - a_point.x_coord, 2) \
     + pow(b_point.y_coord - a_point.y_coord, 2))

class Point:
    """defines a class for point"""
    def __init__(self, x_coord, y_coord):
        assert isinstance(x_coord, float)
        assert isinstance(y_coord, float)
        self.x_coord = x_coord
        self.y_coord = y_coord

    def get_x_coord(self):
        """returns x coordinate"""
        return self.x_coord

    def get_y_coord(self):
        """returns y coordinate"""
        return self.y_coord

class Circle:
    """Implenets class for circle"""
    def __init__(self, center, radius):
        assert isinstance(center, Point)
        assert isinstance(radius, float)
        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        """finds relative positions"""
        assert isinstance(circle, Circle)
        absol = abs(distance(self.center, circle.center))
        radius_sum = self.radius + circle.radius
        radius_sub = abs(self.radius - circle.radius)
        # Same
        if self.center.x_coord == circle.center.x_coord and \
         self.center.y_coord == circle.center.y_coord:
            return RelativePosition.SAME
        # No common points
        if absol > radius_sum or absol < radius_sub:
            return RelativePosition.NO_COMMON_POINTS
        # Touching
        if absol in (radius_sum, radius_sub):
            return RelativePosition.TOUCHING
        # Intersecting
        if radius_sub < absol < radius_sum:
            return RelativePosition.INTERSECTING
        raise ValueError('A very specific case happened')

    def get_center(self):
        """retuns center point"""
        return self.center

    def get_radius(self):
        """retuns radius"""
        return self.radius
