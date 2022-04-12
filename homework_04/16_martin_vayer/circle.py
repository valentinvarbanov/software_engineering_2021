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
    def __init__(self, center, radius):
        assert isinstance(center, Point) and isinstance(radius, float)
        self.center = center
        self.radius = radius

    def find_relative_position(self, circle2):
        assert isinstance(circle2, Circle)

        centers_distance = sqrt(pow((self.center.x - circle2.center.x), 2) +
                                pow((self.center.y - circle2.center.y), 2))

        if (self.center.x == circle2.center.x and self.center.y == circle2.center.y and self.radius == circle2.radius):
            return RelativePosition.SAME
        elif (abs(self.radius - circle2.radius) < centers_distance < self.radius + circle2.radius):
            return RelativePosition.INTERSECTING
        elif centers_distance == self.radius + circle2.radius or centers_distance == (abs(self.radius - circle2.radius)):
            return RelativePosition.TOUCHING
        else:
            return RelativePosition.NO_COMMON_POINTS
