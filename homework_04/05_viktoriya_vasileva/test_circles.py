"""
Tests for class  Circle
"""

from circles import Point, Circle, RelativePosition


def test_outside_circles():
    """
    Tests for circles with no common points
    """
    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(10.0, 10.0), 2.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.NO_COMMON_POINTS

    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(10.0, 1.0), 7.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.NO_COMMON_POINTS

    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(10.0, 1.0), 7.99999)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.NO_COMMON_POINTS



def test_touching_circles():
    """
    Tests for circles touching
    """
    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(1.0, 3.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING

    circle_a = Circle(Point(2.3, 1.0), 1.0)
    circle_b = Circle(Point(2.3, 9.0), 7.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING

    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(10.0, 1.0), 7.999999) #rounding
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING

    circle_a = Circle(Point(2.0, 0.0), 1.0)
    circle_b = Circle(Point(0.0, 0.0), 3.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING


def test_intersecting_circles():
    """
    Tests for circles which are intersecting
    """
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(0.0, 3.0), 3.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.INTERSECTING

    circle_a = Circle(Point(2.3, 1.0), 1.0)
    circle_b = Circle(Point(2.3, 9.87745), 9.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.INTERSECTING

    circle_a = Circle(Point(1.0, 1.0), 1.0)
    circle_b = Circle(Point(0.0, 0.0), 1.5)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.INTERSECTING




def test_same_circles():
    """
    Tests for circles which are the same or are in one another
    """
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(0.0, 0.0), 3.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME

    circle_a = Circle(Point(1.0, 2.0), 1.0)
    circle_b = Circle(Point(1.0, 3.0), 5.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME

    circle_a = Circle(Point(2.0, 1.0), 10.0)
    circle_b = Circle(Point(6.0, 1.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME

    circle_a = Circle(Point(1.0, 10.0), 100.0)
    circle_b = Circle(Point(0.0, 20.0), 1.5)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME

    circle_a = Circle(Point(9.0, 10.0), 100.0)
    circle_b = Circle(Point(0.0, 25.0), 1.5)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME
