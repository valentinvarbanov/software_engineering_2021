'''
Test file that contains multiple unit tests for proving the
circle.py file functionalities
'''

from circle import Circle, Point, RelativePosition

def test_no_common_points():
    '''
    This test checks if 2 initialized circles have no common points'
    Two circles have no common points if their centers distance is bigger
    than the sum of their radii
    '''

    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(4.00001, 0.0), 2.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS

    circle_1 = Circle(Point(1.0, 2.0), 2.97)
    circle_2 = Circle(Point(5.0, 4.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS

    circle_1 = Circle(Point(-3.0, 2.0), 2.3)
    circle_2 = Circle(Point(5.0, -1.0), 1.8)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS

def test_touching():
    '''
    Touching circles have exactly only 1 common point, so the way
    we test this case is by comparing if the centers' distance is
    equal to the sum of the radii
    '''

    circle_1 = Circle(Point(-2.0, 0.0), 2.0)
    circle_2 = Circle(Point(2.0, 0.0), 2.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.TOUCHING

    circle_1 = Circle(Point(0.0, 1.5), 2.5)
    circle_2 = Circle(Point(0.0, -1.5), 0.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.TOUCHING

def test_intersecting():
    '''
    Intersecting points have more than 1 common point, but not all of them.
    In this case we check if the centers euclidean distance is smaller than
    the radii sum, but it's still bigger than the radii difference.
    '''

    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(3.0, 0.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

    circle_1 = Circle(Point(1.0, 2.0), 3.0)
    circle_2 = Circle(Point(-1.0, -3.0), 5.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

    circle_1 = Circle(Point(-3.0, 2.0), 2.2)
    circle_2 = Circle(Point(-4.0, -1.0), 4.4)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

def test_same():
    '''
    We consider two circles to be the same if one circle contains the whole
    set of points the second circle has. This means the centers' euclidean
    distance must be smaller than the radii difference
    '''

    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(0.0, 0.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME

    circle_1 = Circle(Point(1.0, 1.0), 3.0)
    circle_2 = Circle(Point(1.5, 1.0), 2.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME

    circle_1 = Circle(Point(-2.0, -2.0), 5.0)
    circle_2 = Circle(Point(-1.0, -1.0), 1.8)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME
