"""Test the logic from the main task in Homework 3."""

import pytest


from task import Point, Circle
from task import RelativePosition


@pytest.fixture(name='circle_1')
def fixture_circle_1() -> Circle:
    """Return an example circle."""
    return Circle(Point(0.0, 0.0), 3.0)


@pytest.fixture(name='circle_2')
def fixture_circle_2() -> Circle:
    """Return an example circle."""
    return Circle(Point(0.0, 0.0), 1.0)


@pytest.fixture(name='circle_3')
def fixture_circle_3() -> Circle:
    """Return an example circle."""
    return Circle(Point(0.0, 0.0), 7.0)


def test_circles_no_common_points(circle_1, circle_2) -> None:
    """Test if two circle have no points between themselves."""
    assert isinstance(circle_1, Circle)
    assert isinstance(circle_2, Circle)

    circle_smaller = Circle(Point(1.0, 1.0), 1.0)
    circle_bigger = Circle(Point(3.0, 3.0), 9.0)
    circle_outside = Circle(Point(7.0, 7.0), 1.0)

    result = RelativePosition.NO_COMMON_POINTS

    assert circle_1.find_relative_position(circle_2) == result
    assert circle_1.find_relative_position(circle_smaller) == result
    assert circle_1.find_relative_position(circle_bigger) == result
    assert circle_1.find_relative_position(circle_outside) == result


def test_circles_touching(circle_1) -> None:
    """Test if two circles are touching themselves."""
    assert isinstance(circle_1, Circle)

    circle_inside = Circle(Point(0.0, 2.0), 1.0)
    circle_outside = Circle(Point(0.0, 4.0), 1.0)

    result = RelativePosition.TOUCHING

    assert circle_1.find_relative_position(circle_inside) == result
    assert circle_1.find_relative_position(circle_outside) == result


def test_circles_intersecting(circle_1) -> None:
    """Test if two circles are intersecting each other."""
    assert isinstance(circle_1, Circle)

    circle_intersect_1 = Circle(Point(1.0, 0.0), 3.0)
    circle_intersect_2 = Circle(Point(0.0, 1.0), 3.0)

    result = RelativePosition.INTERSECTING

    assert circle_1.find_relative_position(circle_intersect_1) == result
    assert circle_1.find_relative_position(circle_intersect_2) == result


def test_circles_same(circle_1, circle_2, circle_3) -> None:
    """Test of two circles are same."""
    assert isinstance(circle_1, Circle)
    assert isinstance(circle_2, Circle)
    assert isinstance(circle_3, Circle)

    result = RelativePosition.SAME

    assert circle_1.find_relative_position(circle_1) == result
    assert circle_2.find_relative_position(circle_2) == result
    assert circle_3.find_relative_position(circle_3) == result


def test_invalid_input() -> None:
    """Test Circle.find_relative_position() with invalid input data."""
    with pytest.raises(AssertionError):
        Circle(Point(3.0, 3.0), 3.0).find_relative_position(0.0)
