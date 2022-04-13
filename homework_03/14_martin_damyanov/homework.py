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
        print("Given arguments aren't points")
        exit()

    return math.sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))

class Point:
    def __init__(self, x, y):
        try:
            assert isinstance(x, float)
            assert isinstance(y, float)
        except:
            print("Coordinates have to be float")
            exit()
        
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        try:
            assert isinstance(center, Point)
        except:
            print("Given argument isn't point")
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
            print("Given argument isn't circle")
            exit()
          
        # Same
        if self.center.x == circle.center.x and self.center.y == circle.center.y:
            return RelativePosition.SAME
        
        absol = abs(distance(self.center, circle.center))
        radius_sum = self.radius + circle.radius
        radius_sub = abs(self.radius - circle.radius)
        
        # No common points
        if absol > radius_sum or absol < radius_sub:
            return RelativePosition.NO_COMMON_POINTS

        # Touching
        if absol == radius_sum or absol == radius_sub:
            return RelativePosition.TOUCHING

        # Intersecting
        if radius_sub < absol < radius_sum:
            return RelativePosition.INTERSECTING