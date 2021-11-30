import pytest


from task import Point, Circle
from task import RelativePosition


@pytest.fixture
def circle_1() -> Circle:
    return Circle(Point(0.0, 0.0), 3.0)


@pytest.fixture
def circle_2() -> Circle:
    return Circle(Point(0.0, 0.0), 1.0)


@pytest.fixture
def circle_3() -> Circle:
    return Circle(Point(0.0, 0.0), 7.0)


def test_circles_no_common_points(circle_1, circle_2) -> None:
    assert isinstance(circle_1, Circle)
    assert isinstance(circle_2, Circle)

    circle_smaller = Circle(Point(1.0, 1.0), 1.0)
    circle_bigger = Circle(Point(3.0, 3.0), 9.0)
    circle_outside = Circle(Point(7.0, 7.0), 1.0)

    assert circle_1.find_relative_position(circle_2) == RelativePosition.NO_COMMON_POINTS
    assert circle_1.find_relative_position(circle_smaller) == RelativePosition.NO_COMMON_POINTS
    assert circle_1.find_relative_position(circle_bigger) == RelativePosition.NO_COMMON_POINTS
    assert circle_1.find_relative_position(circle_outside) == RelativePosition.NO_COMMON_POINTS


def test_circles_touching(circle_1) -> None:
    assert isinstance(circle_1, Circle)

    circle_inside = Circle(Point(0.0, 2.0), 1.0)
    circle_outside = Circle(Point(0.0, 4.0), 1.0)

    assert circle_1.find_relative_position(circle_inside) == RelativePosition.TOUCHING
    assert circle_1.find_relative_position(circle_outside) == RelativePosition.TOUCHING


def test_circles_intersecting(circle_1) -> None:
    assert isinstance(circle_1, Circle)

    circle_intersect_1 = Circle(Point(1.0, 0.0), 3.0)
    circle_intersect_2 = Circle(Point(0.0, 1.0), 3.0)

    assert circle_1.find_relative_position(circle_intersect_1) == RelativePosition.INTERSECTING
    assert circle_1.find_relative_position(circle_intersect_2) == RelativePosition.INTERSECTING


def test_circles_same(circle_1, circle_2, circle_3) -> None:
    assert isinstance(circle_1, Circle)
    assert isinstance(circle_2, Circle)
    assert isinstance(circle_3, Circle)

    assert circle_1.find_relative_position(circle_1) == RelativePosition.SAME
    assert circle_2.find_relative_position(circle_2) == RelativePosition.SAME
    assert circle_3.find_relative_position(circle_3) == RelativePosition.SAME


def test_invalid_input() -> None:
    with pytest.raises(AssertionError):
        Circle(Point(3.0, 3.0), 3.0).find_relative_position(0.0)
