import enum
import math

class RelativePosition(enum.Enum):
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    #TOUCHING_INTERNALLY = 3
    SAME = 3

class Point:
    def __init__(self, x, y):
        assert isinstance(x, float) 
        assert isinstance(y, float)
        self.x = x
        self.y = y

    def line(self, point):
        assert isinstance(point, Point)
        result = round(math.sqrt( math.pow(point.x - self.x, 2) + math.pow(point.y - self.y, 2)), 5)
        return result
        
class Circle:
    def __init__(self, point, r):
        assert isinstance(point, Point)
        assert isinstance(r, float)
        assert round(r, 5) > 0
        self.point = point
        self.r = r

    def find_relative_position(self, circle):
        assert isinstance(circle, Circle)

       #common center
        if self.point.x == circle.point.x and self.point.y == circle.point.y:
            return RelativePosition.SAME

        AB = self.point.line(circle.point) # >=0
        radius = round(self.r + circle.r, 5)
        #no common points
        if AB > radius:
            return RelativePosition.NO_COMMON_POINTS
        #touching
        if AB == radius:
            return RelativePosition.TOUCHING
        
        radius_sub = self.r - circle.r
        if radius_sub < 0:
            radius_sub = -radius_sub

        #same
        if radius_sub == 0 and AB == 0:
            return RelativePosition.SAME

        #intersect
        if radius_sub < AB and AB < radius:
            return RelativePosition.INTERSECTING

 
        #touching internally
        if AB == radius_sub:
            return RelativePosition.TOUCHING

        # same
        if AB < radius_sub:
            return RelativePosition.SAME
        
            

