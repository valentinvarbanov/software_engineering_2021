from enum import Enum
from math import sqrt
 
class RelativePosition(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def same_center(self, other_circle):
        return (other_circle.center.x == self.center.x) and (other_circle.center.y == self.center.y)

    def distance(self, other_circle):
        return abs(sqrt((other_circle.center.x - self.center.x)**2 + (other_circle.center.y - self.center.y)**2))

    def are_same(self, other_circle):
        if(abs(self.r - other_circle.r) == self.distance(other_circle)):
            return True
        
        if(abs(self.r - other_circle.r) > self.distance(other_circle)):
            return True

        return((other_circle.r == self.r) and self.same_center(other_circle))
        

    def are_not_touching(self, other_circle):
        return(self.r + other_circle.r < self.distance(other_circle))
    
    def are_touching(self, other_circle):
        return(self.r + other_circle.r == self.distance(other_circle))


    def find_relative_position(self, other_circle):
        if(self.are_same(other_circle)):
            return RelativePosition.SAME

        if(self.are_touching(other_circle)):
            return RelativePosition.TOUCHING
        
        if(self.are_not_touching(other_circle)):
            return RelativePosition.NO_COMMON_POINTS

        return RelativePosition.INTERSECTING
        

