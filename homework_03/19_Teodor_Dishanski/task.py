from enum import Enum


class RelativePosition(Enum):
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


    def __eq__(self, other_point) -> bool:
        assert isinstance(other_point, Point)
        return self.x == other_point.x and self.y == other_point.y


    def distance(self, other_point) -> float:
        assert isinstance(other_point, Point)
        result_x = self.x - other_point.x
        result_y = self.y - other_point.y
        return (result_x ** 2 + result_y ** 2) ** 0.5


class Circle:
    def __init__(self, center, r) -> None:
        assert isinstance(center, Point)
        assert isinstance(r, float)
        assert r > 0

        self.center = center
        self.r = r


    def __eq__(self, other_circle) -> bool:
        assert isinstance(other_circle, Circle)
        return self.center == other_circle.center and self.r == other_circle.r


    def find_relative_position(self, other_circle) -> RelativePosition:
        assert isinstance(other_circle, Circle)

        distance_centers = self.center.distance(other_circle.center)
        radii_sum = self.r + other_circle.r
        radii_diff = abs(self.r - other_circle.r)

        if self == other_circle:
            return RelativePosition.SAME
        else:
            if abs(distance_centers - radii_sum) < 0.001 or abs(distance_centers - radii_diff) < 0.001:
                return RelativePosition.TOUCHING
            elif distance_centers > radii_sum or distance_centers < radii_diff:
                return RelativePosition.NO_COMMON_POINTS
            else:
                return RelativePosition.INTERSECTING
