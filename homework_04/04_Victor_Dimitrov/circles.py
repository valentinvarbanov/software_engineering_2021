'''
This file provides simple points and circles logic
'''

from enum import Enum
from math import sqrt

#pylint: disable=R0903

class RelativePosition(Enum):
    '''
    Enum that has all the possible combinations of positions
    between two given circles
    '''

    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

class Point:
    '''
    Simple 2D plane point with 2 coordinates
    '''

    def __init__(self, coord_x, coord_y):
        assert(isinstance(coord_x, float) and isinstance(coord_y, float))

        self.coord_x = coord_x
        self.coord_y = coord_y

    def euclidean_distance(self, other):
        '''
        It's handy to have an euclidean distance function instead of writing
        it every time you need the euclidean distance between two points.
        Source: https://www.cuemath.com/euclidean-distance-formula/
        '''

        assert isinstance(other, Point)

        diff_x = self.coord_x - other.coord_x
        diff_y = self.coord_y - other.coord_y

        return sqrt(diff_x ** 2 + diff_y ** 2)

class Circle:
    '''
    Circle class that resembles the definition of a circle as a
    figure - it has a radius and central point
    '''

    def __init__(self, center, radius):
        assert(isinstance(center, Point) and isinstance(radius, float) and radius > 0)

        self.center = center
        self.radius = radius

    def circle_position(self, other_circle):
        '''
        In this function we determine if 2 circles have one, many or zero common points
        based on their centers' euclidean distance and sum/difference of their respective radii
        '''

        assert isinstance(other_circle, Circle)

        added_radiuses = self.radius + other_circle.radius
        substracted_radiuses = abs(self.radius - other_circle.radius)

        centers_distance = self.center.euclidean_distance(other_circle.center)

        position = None

        if centers_distance > added_radiuses:
            position = RelativePosition.NO_COMMON_POINTS

        elif centers_distance == added_radiuses:
            position = RelativePosition.TOUCHING

        elif substracted_radiuses < centers_distance < added_radiuses:
            position = RelativePosition.INTERSECTING

        else:
            position = RelativePosition.SAME

        return position
    