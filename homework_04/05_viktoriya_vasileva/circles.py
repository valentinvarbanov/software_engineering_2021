# pylint: disable=invalid-name
#pylint: disable=R0903
#pylint: disable=C0303
#pylint: disable=C0103
#pylint: disable=R0911
#pylint: disable=C1001
"""
    This module has Point and Circle classes
    The Circle class has function for finding
    the position between two cicles
"""

import enum
import math

class RelativePosition(enum.Enum):
    """
        This class is Enum
        It is used for the class Circle
    """
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    #TOUCHING_INTERNALLY = 3
    SAME = 3

class Point(object):
    """
        This class is point
        Point is used for coordinated system.
    """
    def __init__(self, x, y):
        """
        Initializes the instance and
        assures that the arguments are right
        """
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y

    def line(self, point):
        """
        Find the length of the line
        """
        assert isinstance(point, Point)
        result = round(math.sqrt(math.pow(point.x - self.x, 2) + math.pow(point.y - self.y, 2)), 5)
        return result

class Circle(object):
    """
        Circle is point in coordinated system with radius
    """
    def __init__(self, point, r):
        """
        Initializes the instance and
        assures that the arguments are right
        """
        assert isinstance(point, Point)
        assert isinstance(r, float)
        assert round(r, 5) > 0
        self.point = point
        self.r = r

    def find_relative_position(self, circle):
        """
        Finds the position between this circle and the given
        """
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
        return None
