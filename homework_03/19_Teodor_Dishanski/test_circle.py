import pytest

from task import Point, Circle


def test_valid_circle_instance() -> None:
    circle = Circle(Point(0.0, 0.0), 1.0)
    assert isinstance(circle, Circle)
    assert circle.center == Point(0.0, 0.0)
    assert circle.r == 1.0


def test_circles_equality():
    circle1 = Circle(Point(0.0, 0.0), 1.0)
    circle2 = Circle(Point(3.0, 3.0), 1.0)
    circle3 = Circle(Point(0.0, 0.0), 1.0)
    circle4 = Circle(Point(3.0, 3.0), 1.0)

    assert circle1 == circle3
    assert circle1 != circle2
    assert circle1 != circle4

    assert circle2 == circle4
    assert circle2 != circle1
    assert circle2 != circle3

    assert circle3 == circle1
    assert circle3 != circle2
    assert circle3 != circle4

    assert circle4 == circle2
    assert circle4 != circle1
    assert circle4 != circle3


def test_invalid_circle_instance() -> None:
    with pytest.raises(AssertionError):
        Circle(Point(0.0, 0.0), 1)


def test_invalid_circle_equality() -> None:
    with pytest.raises(AssertionError):
        Circle(Point(0.0, 0.0), 1.0) == 0
