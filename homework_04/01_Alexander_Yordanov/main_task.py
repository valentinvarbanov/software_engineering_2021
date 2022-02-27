#pylint: disable=R0903
#pylint: disable=C0303
#pylint: disable=C0103

import math
from enum import Enum

'''
Enum types for all the positions 
'''

class ReturnTypes(Enum):
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4

'''
Point object 
'''

class Point: 
    def __init__(self, x, y) -> None:
        assert isinstance(x, float)
        assert isinstance(y, float)

        self.x = x
        self.y = y

'''
Circle object 
'''

class Circle:
    def __init__(self, center, radius) -> None:
        assert isinstance(center, Point)

        self.center = center
        self.radius = radius

    '''
    Find the relative position function 
    '''

    def find_relative_position(self, another_circle):
        assert isinstance(another_circle, Circle)

        distance = math.sqrt((another_circle.center.x - self.center.x) ** 2 + \
            (another_circle.center.y - self.center.y) ** 2)
        
        sumOfTheRadius = self.radius + another_circle.radius
        subOfTheRadius = self.radius - another_circle.radius


        '''
        All the case we have to check for positions.
        '''

        if self.center.x == another_circle.center.x and self.center.y == another_circle.center.y \
            or abs(distance) < abs(subOfTheRadius):
            return ReturnTypes.SAME

        elif abs(distance) > sumOfTheRadius:
            return ReturnTypes.NO_COMMON_POINTS

        elif abs(distance) == sumOfTheRadius or abs(distance) == abs(subOfTheRadius):
            return ReturnTypes.TOUCHING

        elif abs(subOfTheRadius) < abs(distance) < sumOfTheRadius:
            return ReturnTypes.INTERSECTING