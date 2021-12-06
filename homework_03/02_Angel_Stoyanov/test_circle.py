from Point import Point
from Circle import Circle
from RelativePosition import RelativePosition

def test_position_should_be_intersecting():
    circle_a = Circle(Point(3.0, 4.0), 2.0)
    circle_b = Circle(Point(1.0, 2.0), 2.0)
    assert circle_a.get_position(circle_b) == RelativePosition.INTERSECTING
    assert circle_b.get_position(circle_a) == RelativePosition.INTERSECTING

def test_position_should_be_same():
    # Same circles
    circle_a = Circle(Point(3.0, 4.0), 2.0)
    circle_b = Circle(Point(3.0, 4.0), 2.0)
    assert circle_a.get_position(circle_b) == RelativePosition.SAME
    assert circle_b.get_position(circle_a) == RelativePosition.SAME

    # Same circles but with different radius
    circle_a = Circle(Point(5.0, 15.0), 2.0)
    circle_b = Circle(Point(5.0, 15.0), 4.0)
    assert circle_a.get_position(circle_b) == RelativePosition.SAME
    assert circle_b.get_position(circle_a) == RelativePosition.SAME

    # Should fail
    circle_b = Circle(Point(6.0, 15.0), 2.0)
    assert circle_a.get_position(circle_b) != RelativePosition.SAME

def test_position_should_be_no_common_points():
    circle_a = Circle(Point(1.0, 3.0), 0.5)
    circle_b = Circle(Point(6.5, 6.0), 2.0)
    assert circle_a.get_position(circle_b) == RelativePosition.NO_COMMON_POINTS
    assert circle_b.get_position(circle_a) == RelativePosition.NO_COMMON_POINTS

def test_position_should_be_touching():
    circle1 = Circle(Point(2.0, 1.0), 1.0)
    circle2 = Circle(Point(4.0, 1.0), 1.0)
    assert circle1.get_position(circle2) == RelativePosition.TOUCHING

    circle1 = Circle(Point(-1.0, 3.0), 3.0)
    circle2 = Circle(Point(3.0, 3.0), 1.0)
    assert circle1.get_position(circle2) == RelativePosition.TOUCHING