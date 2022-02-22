"""Pytests"""

from main import *


def test_no_common():
    """Tests for no common points"""
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(5.0, 5.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.NO_COMMON_POINTS

    circle_a = Circle(Point(3.4, 6.3), 13.8)
    circle_b = Circle(Point(54.89, 0.6), 3.89)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.NO_COMMON_POINTS


def test_touching():
    """Tests for if the circles are touching"""
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(0.0, 2.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING

    circle_a = Circle(Point(3.3, 4.3), 1.0)
    circle_b = Circle(Point(6.3, 4.3), 2.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.TOUCHING


def test_intersecting():
    """Tests for if the circles are intersecting"""
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(1.0, 1.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.INTERSECTING

    circle_a = Circle(Point(0.4444, 16.7), 3.35)
    circle_b = Circle(Point(1.8347, 14.89), 4.88)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.INTERSECTING


def test_same():
    """Tests for if the circles are the same"""
    circle_a = Circle(Point(0.0, 0.0), 1.0)
    circle_b = Circle(Point(0.0, 0.0), 1.0)
    assert circle_a.find_relative_position(circle_b) == RelativePosition.SAME


test_same()
test_intersecting()
test_touching()
test_no_common()
