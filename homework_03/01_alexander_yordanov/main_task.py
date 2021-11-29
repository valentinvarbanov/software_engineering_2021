import math
from enum import Enum

class ReturnTypes(Enum):
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
    def __init__(self, center, r) -> None:
        assert isinstance(center, Point)

        self.center = center
        self.r = r

    def find_relative_position(self, another_circle):
        assert isinstance(another_circle, Circle)

        distance = math.sqrt((another_circle.center.x - self.center.x) ** 2 + (another_circle.center.y - self.center.y) ** 2)
        radiusSum = self.r + another_circle.r
        radiusSub = self.r - another_circle.r

        if distance == 0 and radiusSub == 0:
            return ReturnTypes.SAME

        elif abs(distance) > radiusSum:
            return ReturnTypes.NO_COMMON_POINTS

        elif abs(distance) == radiusSum or abs(distance) == abs(radiusSub):
            return ReturnTypes.TOUCHING

        elif abs(radiusSub) < abs(distance) < radiusSum:
            return ReturnTypes.INTERSECTING