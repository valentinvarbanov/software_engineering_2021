import enum
from math import sqrt

class RelativePosition(enum.Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance_between_two_centers(center_1, center_2):
        return sqrt(pow((center_1.x - center_2.x), 2) + pow((center_1.y - center_2.y), 2))
        
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)
        assert radius > 0

    def find_relative_position(self, circle_2):
        distance = Point.distance_between_two_centers(self.center, circle_2.center)
        sum_radiuses = self.radius + circle_2.radius
        sub_radiuses = abs(self.radius - circle_2.radius)

        if(distance > sum_radiuses):
            return RelativePosition.NO_COMMON_POINTS
        elif(distance == sum_radiuses):
            return RelativePosition.TOUCHING
        elif(sub_radiuses < distance and distance < sum_radiuses):
            return RelativePosition.INTERSECTING
        elif(distance <= sub_radiuses or self.center == circle_2.center):
            return RelativePosition.SAME