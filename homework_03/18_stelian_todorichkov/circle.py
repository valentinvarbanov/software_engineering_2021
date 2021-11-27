from enum import Enum
from math import sqrt

class RealativePosition(Enum):
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3

class Point:
    def __init__(self, x, y):
        assert isinstance(x, float)
        assert isinstance(y, float)
        
        self.x = x
        self.y = y

    def __eq__(self, other):
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y

    def distane_between_points(self, other):
        assert isinstance(other, Point)
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return sqrt(sub_x ** 2 + sub_y ** 2)

class Circle:
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
        assert isinstance(other, Circle)
        distance = self.center.distane_between_points(other.center)
        if self == other:
            return RealativePosition.SAME
        elif abs(self.radius - other.radius) < distance < (self.radius + other.radius):
            return RealativePosition.INTERSECTING
        elif distance == (self.radius + other.radius) or distance == abs(self.radius - other.radius):
            return RealativePosition.TOUCHING
        else:
            return RealativePosition.NO_COMMON_POINTS