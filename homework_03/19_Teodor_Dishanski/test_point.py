import pytest

from task import Point


def test_valid_point_instance() -> None:
    point = Point(0.0, 0.0)
    assert isinstance(point, Point)
    assert point.x == 0.0
    assert point.y == 0.0


def test_points_equality() -> None:
    point_1 = Point(0.0, 0.0)
    point_2 = Point(3.0, 3.0)
    point_3 = Point(0.0, 0.0)
    point_4 = Point(3.0, 3.0)

    assert point_1 == point_3
    assert point_1 != point_2
    assert point_1 != point_4

    assert point_2 == point_4
    assert point_2 != point_1
    assert point_2 != point_3

    assert point_3 == point_1
    assert point_3 != point_2
    assert point_3 != point_4

    assert point_4 == point_2
    assert point_4 != point_1
    assert point_4 != point_3


def test_distance_points() -> None:
    point_1 = Point(0.0, 0.0)
    point_2 = Point(1.0, 1.0)
    point_3 = Point(0.0, 1.0)
    point_4 = Point(1.0, 0.0)
    point_5 = Point(3.0, 3.0)

    assert point_1.distance(point_1) == 0.0
    assert point_1.distance(point_2) == 2 ** 0.5
    assert point_1.distance(point_3) == 1.0
    assert point_1.distance(point_4) == 1.0
    assert point_1.distance(point_5) == 18 ** 0.5

    assert point_2.distance(point_1) == 2 ** 0.5
    assert point_2.distance(point_2) == 0.0
    assert point_2.distance(point_3) == 1.0
    assert point_2.distance(point_4) == 1.0
    assert point_2.distance(point_5) == 8 ** 0.5

    assert point_3.distance(point_1) == 1.0
    assert point_3.distance(point_2) == 1.0
    assert point_3.distance(point_3) == 0.0
    assert point_3.distance(point_4) == 2 ** 0.5
    assert point_3.distance(point_5) == 13 ** 0.5

    assert point_4.distance(point_1) == 1.0
    assert point_4.distance(point_2) == 1.0
    assert point_4.distance(point_3) == 2 ** 0.5
    assert point_4.distance(point_4) == 0.0
    assert point_4.distance(point_5) == 13 ** 0.5

    assert point_5.distance(point_1) == 18 ** 0.5
    assert point_5.distance(point_2) == 8 ** 0.5
    assert point_5.distance(point_3) == 13 ** 0.5
    assert point_5.distance(point_4) == 13 ** 0.5
    assert point_5.distance(point_5) == 0.0


def test_invalid_point_instance() -> None:
    with pytest.raises(AssertionError):
        Point(0, 0)


def test_invalid_points_equality() -> None:
    with pytest.raises(AssertionError):
        assert Point(0.0, 1.0) == 0


def test_invalid_points_distance() -> None:
    with pytest.raises(AssertionError):
        Point(0.0, 0.0).distance(0.0)
