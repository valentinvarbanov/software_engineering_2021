from enum import Enum
from math import fabs, sqrt

#pylint: disable=R0903

def find_distance(a, b):
    sideA = fabs(a.x - b.x)
    sideB = fabs(a.y - b.y)
    return sqrt((sideB * sideB) + (sideA * sideA))


class RelativePosition(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4


class Point:
    def __init__(self, x, y) -> None:
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y


class Circle:
    def __init__(self, X, r) -> None:
        assert isinstance(X, Point)
        assert isinstance(r, float)
        self.X = X
        self.r = r

    def find_relative_position(self, another):
        assert isinstance(another, Circle)

        AB = find_distance(self.X, another.X)
        position = RelativePosition.SAME

        if AB > (self.r + another.r):
            position = RelativePosition.NO_COMMON_POINTS

        elif AB == (self.r + another.r) or (AB == fabs((self.r - another.r)) and AB != 0):
            position = RelativePosition.TOUCHING

        elif (self.r + another.r) > AB > fabs((self.r - another.r)):
            position = RelativePosition.INTERSECTING

        return position