from enum import Enum
from math import sqrt

class RelativePosition(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

class Point:

    def __init__(self, x, y):
        assert(isinstance(x, float) and isinstance(y, float))    

        self.x = x
        self.y = y  

    def euclidean_distance(self, other):
        assert isinstance(other, Point)    

        diff_x = self.x - other.x
        diff_y = self.y - other.y

        return sqrt(diff_x ** 2 + diff_y ** 2)            

class Circle:

    def __init__(self, center, radius):
        assert(isinstance(center, Point) and isinstance(radius, float) and radius > 0)

        self.center = center
        self.radius = radius

    def circle_position(self, other_circle):
        assert isinstance(other_circle, Circle)

        added_radiuses = self.radius + other_circle.radius
        substracted_radiuses = abs(self.radius - other_circle.radius)

        centers_distance = self.center.euclidean_distance(other_circle.center)           

        if centers_distance > added_radiuses:
            return RelativePosition.NO_COMMON_POINTS

        elif centers_distance == added_radiuses:
            return RelativePosition.TOUCHING

        elif substracted_radiuses < centers_distance and centers_distance < added_radiuses:
            return RelativePosition.INTERSECTING

        else:
            return RelativePosition.SAME            

