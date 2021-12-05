import enum
from math import sqrt, pow

class RelativePosition(enum.Enum):
    NO_COMMON_POINTS = -1
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 0

class Point():
    def __init__(self, x, y) -> None:
        assert isinstance(x, float)
        assert isinstance(y, float)

        self.x = x
        self.y = y

class Circle():
    def __init__(self, center, radius) -> None:
        assert isinstance(center, Point)
        assert isinstance(radius, float)

        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        assert isinstance(circle, Circle)
        if circle.center.x == self.center.x and circle.center.y == self.center.y:
            return RelativePosition.SAME
        else:
            distance = sqrt(pow(circle.center.x - self.center.x, 2) + pow(circle.center.y - self.center.y, 2))
            if distance > self.radius + circle.radius:
                return RelativePosition.NO_COMMON_POINTS
            elif abs(distance - (self.radius + circle.radius)) < 0.0001:
                return RelativePosition.TOUCHING
            else: #distance < self.radius + circle.radius:
                if distance + circle.radius < self.radius or (distance + circle.radius) - self.radius < 0.0001:
                    return RelativePosition.SAME
                else:
                    return RelativePosition.INTERSECTING

circle1 = Circle(Point(0.0, 0.0), 10.0)
circle2 = Circle(Point(4.0, 0.0), 6.0)
print(circle1.find_relative_position(circle2))