from enum import Enum, auto
from math import sqrt, pow

class RelativePosition(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4


class Point:

    def __init__(self, x, y):
        assert isinstance(x, float) and isinstance(y, float)
        self.x = x
        self.y = y


class Circle:

    def __init__(self, center, r):
        assert isinstance(center, Point) and isinstance(r, float)
        self.center = center
        self.r = r

    def find_relative_position(self, second_circle):
        assert isinstance(second_circle, Circle)


        centers_distance = sqrt( pow((self.center.x - second_circle.center.x), 2) + pow((self.center.y - second_circle.center.y), 2) )


        if (self.center.x == second_circle.center.x and self.center.y == second_circle.center.y and self.r == second_circle.r):
            return RelativePosition.SAME
            
        elif (abs(self.r - second_circle.r) < centers_distance <  self.r + second_circle.r):
            return RelativePosition.INTERSECTING
            
        elif centers_distance == self.r + second_circle.r or centers_distance == (abs(self.r - second_circle.r)):
            return RelativePosition.TOUCHING]
            
        else:
            return RelativePosition.NO_COMMON_POINTS

