'''
Main file with all the logic
'''
from enum import Enum
import numpy as np

#pylint: disable=R0903
#pylint: disable=C0303
#pylint: disable=C0103


class RelativePostion(Enum):
    '''
    Enum that has all the possible cases of relations
    between two given circles
    '''

    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3

class Point:
    '''
    Simple 2D plane point with 2 coordinates
    '''

    def __init__(self, x, y) -> None:
        assert isinstance(x, float)
        assert isinstance(y, float)

        self.x = x
        self.y = y

    def __eq__(self, other_point) -> bool:
        assert isinstance(other_point, Point)

        return self.x == other_point.x and self.y == other_point.y

class Circle:
    '''
    Circle class that resembles the definition of a circle as a
    figure - it has a radius and central point
    '''

    def __init__(self, center, radius) -> None:
        assert isinstance(center, Point)
        assert isinstance(radius, float)

        self.center = center
        self.radius = radius

    def __eq__(self, other_circle) -> bool:
        assert isinstance(other_circle, Circle)
        return other_circle.radius == self.radius and other_circle.center == self.center

    def find_relative_position(self, other) -> RelativePostion:
        '''
        In this function we determine the exact relation of two circles expressed
        with the enum above based on their distances and radiuses.
        '''

        assert isinstance(other, Circle)

        if self == other:
            return RelativePostion.SAME

        distance = np.sqrt((other.center.x - self.center.x) ** 2 + \
        (other.center.y - self.center.y) ** 2) # pitagor

        radius_sum = self.radius + other.radius
        radius_difference = abs(self.radius - other.radius)

        if distance == 0 and self.radius == other.radius:
            return RelativePostion.SAME

        if distance > radius_sum or distance < radius_difference:
            return RelativePostion.NO_COMMON_POINTS

        if distance in [radius_sum, radius_difference]:
            return RelativePostion.TOUCHING

        return RelativePostion.INTERSECTING
