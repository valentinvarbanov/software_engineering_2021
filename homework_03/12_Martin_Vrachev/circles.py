from enum import Enum
import math

class RelativePosition(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

def distance(a, b):
    try:
        assert isinstance(a, Point)
        assert isinstance(b, Point)
    except:
        print('The function takes points as parameters!')
        exit()

    return math.sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))

class Point:
    def __init__(self, x, y):
        try:
            assert isinstance(x, float)
            assert isinstance(y, float)
        except:
            print("The point coordinates have to be float!")
            exit()
        
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        try:
            assert isinstance(center, Point)
        except:
            print("The center has to be type Point!")
            exit()

        try:
            assert isinstance(radius, float)
        except:
            print("The radius has to be float!")
            exit()

        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        try:
            assert isinstance(circle, Circle)
        except:
            print('The function takes type Circle as a paramater!')
            exit()
          
        # Same
        if self.center.x == circle.center.x and self.center.y == circle.center.y and self.radius == circle.radius:
            return RelativePosition.SAME
        
        ab = abs(distance(self.center, circle.center))
        radii_sum = self.radius + circle.radius
        radii_sub = abs(self.radius - circle.radius)
        
        # No common points
        if ab > radii_sum or ab < radii_sub:
            return RelativePosition.NO_COMMON_POINTS

        # Touching
        if ab == radii_sum or ab == radii_sub:
            return RelativePosition.TOUCHING

        # Intersecting
        if radii_sub < ab < radii_sum:
            return RelativePosition.INTERSECTING
