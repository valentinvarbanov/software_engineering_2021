'''
Check position of two circles
'''
from enum import Enum
import math
import sys

#pylint: disable=R0903
class RelativePosition(Enum):
    '''
    Enum class used for return statements after checks
    '''

    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

def distance(point_a, point_b):
    '''
    Function which calculates distance between two points
    '''

    try:
        assert isinstance(point_a, Point)
        assert isinstance(point_b, Point)
    except AssertionError:
        print('The function takes points as parameters!')
        sys.exit()

    return math.sqrt(pow(point_b.x_coordinate - point_a.x_coordinate, 2) + \
     pow(point_b.y_coordinate - point_a.y_coordinate, 2))

class Point:
    '''
    Class representing a point in a coordinate system
    '''

    def __init__(self, x_coordinate, y_coordinate):
        try:
            assert isinstance(x_coordinate, float)
            assert isinstance(y_coordinate, float)
        except AssertionError:
            print("The point coordinates have to be float!")
            sys.exit()

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

class Circle:
    '''
    Class representing a circle
    '''
    def __init__(self, center, radius):
        try:
            assert isinstance(center, Point)
        except AssertionError:
            print("The center has to be type Point!")
            sys.exit()

        try:
            assert isinstance(radius, float)
        except AssertionError:
            print("The radius has to be float!")
            sys.exit()

        self.center = center
        self.radius = radius

    def find_relative_position(self, circle):
        '''
        Find relative position of two circles
        '''
        try:
            assert isinstance(circle, Circle)
        except AssertionError:
            print('The function takes type Circle as a paramater!')
            sys.exit()

        # Same
        if self.center.x_coordinate == circle.center.x_coordinate and \
         self.center.y_coordinate == circle.center.y_coordinate and self.radius == circle.radius:
            return RelativePosition.SAME

        a_b = abs(distance(self.center, circle.center))
        radii_sum = self.radius + circle.radius
        radii_sub = abs(self.radius - circle.radius)

        # No common points
        if a_b > radii_sum or a_b < radii_sub:
            return RelativePosition.NO_COMMON_POINTS

        # Touching
        if a_b in (radii_sum, radii_sub):
            return RelativePosition.TOUCHING

        # Intersecting
        if radii_sub < a_b < radii_sum:
            return RelativePosition.INTERSECTING

        return None
