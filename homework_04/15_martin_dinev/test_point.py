"""
File to test if everything is correct
"""

from point import Circle, Point, RelativePosition

def test_no_common_points():
    """
    Test if two circles have no common points
    """
    circle1 = Circle(Point(0.0, 0.0), 3.0)
    circle2 = Circle(Point(10.0, 0.0), 4.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS

    circle1 = Circle(Point(1.2, 3.1), 8.6)
    circle2 = Circle(Point(13.5, 17.2), 10.1)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS

def test_touching():
    """
    Test if two circles are touching
    """
    circle1 = Circle(Point(0.0, 0.0), 4.0)
    circle2 = Circle(Point(10.0, 0.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING

    circle1 = Circle(Point(0.0, 0.0), 4.0)
    circle2 = Circle(Point(0.0, 10.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING

def test_same():
    """
    Test if two circles are the same
    """
    circle1 = Circle(Point(0.0, 0.0), 6.0)
    circle2 = Circle(Point(0.0, 0.0), 4.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME

    circle1 = Circle(Point(0.0, 0.0), 4.0)
    circle2 = Circle(Point(0.0, 0.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME

    circle1 = Circle(Point(0.0, 0.0), 10.0)
    circle2 = Circle(Point(4.0, 0.0), 2.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME

    circle1 = Circle(Point(0.0, 0.0), 10.0)
    circle2 = Circle(Point(4.0, 0.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME

def test_intersecting():
    """
    Test if two circles are intersecting
    """
    circle1 = Circle(Point(0.0, 0.0), 5.0)
    circle2 = Circle(Point(10.0, 0.0), 7.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.INTERSECTING

    circle1 = Circle(Point(1.2, 3.1), 8.6)
    circle2 = Circle(Point(13.5, 17.2), 16.1)
    assert circle1.find_relative_position(circle2) == RelativePosition.INTERSECTING
