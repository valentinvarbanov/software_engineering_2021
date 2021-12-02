from main import *


def test_no_common():
    a = Circle(Point(0.0, 0.0), 1.0)
    b = Circle(Point(5.0, 5.0), 1.0)
    assert a.find_relative_position(b) == RelativePosition.NO_COMMON_POINTS

    a = Circle(Point(3.4, 6.3), 13.8)
    b = Circle(Point(54.89, 0.6), 3.89)
    assert a.find_relative_position(b) == RelativePosition.NO_COMMON_POINTS


def test_touching():
    a = Circle(Point(0.0, 0.0), 1.0)
    b = Circle(Point(0.0, 2.0), 1.0)
    assert a.find_relative_position(b) == RelativePosition.TOUCHING

    a = Circle(Point(3.3, 4.3), 1.0)
    b = Circle(Point(6.3, 4.3), 2.0)
    assert a.find_relative_position(b) == RelativePosition.TOUCHING


def test_intersecting():
    a = Circle(Point(0.0, 0.0), 1.0)
    b = Circle(Point(1.0, 1.0), 1.0)
    assert a.find_relative_position(b) == RelativePosition.INTERSECTING

    a = Circle(Point(0.4444, 16.7), 3.35)
    b = Circle(Point(1.8347, 14.89), 4.88)
    assert a.find_relative_position(b) == RelativePosition.INTERSECTING


def test_same():
    a = Circle(Point(0.0, 0.0), 1.0)
    b = Circle(Point(0.0, 0.0), 1.0)
    assert a.find_relative_position(b) == RelativePosition.SAME

test_same()
test_intersecting()
test_touching()
test_no_common()