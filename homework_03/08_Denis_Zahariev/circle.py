import numpy as np
from enum import Enum

class RelativePostion(Enum):
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3

class Point: 
    def __init__(self, x, y) -> None:
        assert isinstance(x, float)
        assert isinstance(y, float)

        self.x = x
        self.y = y
    
    def __eq__(self, otherPoint) -> bool:
        assert isinstance(otherPoint, Point)

        return self.x == otherPoint.x and self.y == otherPoint.y

class Circle:
    def __init__(self, center, r) -> None:
        assert isinstance(center, Point)
        assert isinstance(r, float)

        self.center = center
        self.r = r

    def __eq__(self, otherCircle) -> bool:
        assert isinstance(otherCircle, Circle)
        return otherCircle.r == self.r and otherCircle.center == self.center

    def find_relative_position(self, other) -> RelativePostion:
        assert isinstance(other, Circle)

        if self == other:
            return RelativePostion.SAME

        distance = np.sqrt((other.center.x - self.center.x) ** 2 + (other.center.y - self.center.y) ** 2) # pitagor

        radius_sum = self.r + other.r
        radius_difference = abs(self.r - other.r)

        if distance == 0 and self.r == other.r:
            return RelativePostion.SAME

        elif distance > radius_sum or distance < radius_difference:
            return RelativePostion.NO_COMMON_POINTS

        elif distance == radius_sum or distance == radius_difference:
            return RelativePostion.TOUCHING
        else:
            return RelativePostion.INTERSECTING 