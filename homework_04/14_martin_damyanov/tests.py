""" Tests functions in homework.py"""

from homework import Point, Circle, RelativePosition, distance #imports homework module

def test_create_point():
    """Tests creating of points"""
    point1 = Point(3.1, 3.5)
    assert isinstance(point1, Point)

def test_create_circle():
    """Tests creating of circle"""
    point = Point(5.4, 4.5)
    circle = Circle(point, 5.0)
    assert isinstance(circle, Circle)

def test_distance():
    """Tests finding of distance"""
    point1 = Point(2.0, 1.0)
    point2 = Point(6.0, 4.0)
    assert distance(point1, point2) == 5.0
    point1 = Point(2.0, -1.0)
    point2 = Point(-2.0, 2.0)
    assert distance(point1, point2) == 5.0

def test_no_common_points():
    """Tests relative position with no common points"""
    circle1 = Circle(Point(2.0, 1.0), 1.0)
    circle2 = Circle(Point(6.0, 4.0), 2.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS
    circle1 = Circle(Point(2.0, 1.0), 9.0)
    circle2 = Circle(Point(6.0, 4.0), 20.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS

def test_touching():
    """Tests relative position with no touching point"""
    circle1 = Circle(Point(2.0, 1.0), 2.0)
    circle2 = Circle(Point(6.0, 4.0), 3.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING
    circle1 = Circle(Point(2.0, 1.0), 16.0)
    circle2 = Circle(Point(6.0, 4.0), 21.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING

def test_intersecting():
    """Tests relative position of intersecting"""
    circle1 = Circle(Point(2.0, 1.0), 5.0)
    circle2 = Circle(Point(6.0, 4.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.INTERSECTING

def test_same():
    """Tests if two circles are the same"""
    circle1 = Circle(Point(2.0, 2.0), 5.0)
    circle2 = Circle(Point(2.0, 2.0), 5.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME
