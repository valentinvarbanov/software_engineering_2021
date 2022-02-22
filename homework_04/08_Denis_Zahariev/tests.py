'''
Test file that contains multiple unit tests for proving the
circle.py file functionalities
'''

from circles import Point, Circle, RelativePostion

#pylint: disable=R0903

# test for point initialization
def test_create_point():
    '''
    This test checks the proper initialization of intance of class Point
    '''
    point = Point(3.0, 2.0)
    assert isinstance(point, Point)

# test for circle initialization
def test_create_circle():
    '''
    This test checks the proper initialization of intance of class Circle
    '''
    center = Point(3.0, 3.0)
    radius = 1.0
    circle = Circle(center, radius)
    assert isinstance(circle, Circle)

def test_same():
    '''
    This test checks the proper comparisson of 2
    circles that have identical radius and center coordinates
    '''

    circle1 = Circle(Point(6.0, 6.0), 6.0)

    assert circle1.find_relative_position(circle1) == RelativePostion.SAME

    # test with another instance
    circle2 = Circle(Point(6.0, 6.0), 6.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.SAME

def test_no_common_points():
    '''
    This test checks the proper comparisson of 2
    circles that are too far from each other and therefore
    not overlapping anywhere
    '''

    circle1 = Circle(Point(0.0, 0.0), 1.0)
    circle2 = Circle(Point(3.0, 3.0), 1.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.NO_COMMON_POINTS

    circle1 = Circle(Point(3.0, -1.0), 1.0)
    circle2 = Circle(Point(5.0, 2.0), 1.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.NO_COMMON_POINTS

    circle1 = Circle(Point(6.0, 6.0), 6.0)
    circle2 = Circle(Point(6.0, 6.0), 5.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.NO_COMMON_POINTS


def test_touching():
    '''
    This test checks the proper comparisson of 2
    circles that are just touching on the plane.
    '''
    # external touch
    circle1 = Circle(Point(3.0, 3.0), 3.0)
    circle2 = Circle(Point(7.0, 6.0), 2.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.TOUCHING

    # internal touch
    circle3 = Circle(Point(0.0, 0.0), 6.0)
    circle4 = Circle(Point(0.0, 3.0), 3.0)

    assert circle3.find_relative_position(circle4) == RelativePostion.TOUCHING

def test_intersecting():
    '''
    This test checks the proper comparisson of 2
    circles that are overlapping on the plane.
    '''
    circle1 = Circle(Point(1.0, 1.0), 3.0)
    circle2 = Circle(Point(2.0, 1.0), 3.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.INTERSECTING
