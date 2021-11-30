from circles import *
import pytest

def test_create_point():
    p1 = Point(5.4, 6.5)
    assert isinstance(p1, Point)

def test_create_invalid_point():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        p2 = Point('koko', 5.7)

    assert pytest_wrapped_e.type == SystemExit

def test_create_circle():
    p = Point(5.5, 4.5)
    c = Circle(p, 10.0)
    assert isinstance(c, Circle)

def test_create_invalid_circle():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        c1 = Circle(5, 6.7)

    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        p = Point(1.2, 8.7)
        c2 = Circle(p, 'radius')

    assert pytest_wrapped_e.type == SystemExit

def test_distance():
    p1 = Point(2.0, 1.0)
    p2 = Point(6.0, 4.0)
    assert distance(p1, p2) == 5.0

    p1 = Point(2.0, -1.0)
    p2 = Point(-2.0, 2.0)
    assert distance(p1, p2) == 5.0

def test_invalid_distance_arguments():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        distance(2,3)
    
    assert pytest_wrapped_e.type == SystemExit

def test_find_realtive_position_invalid_arguments():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        p = Point(5.6, 1.2)
        c = Circle(p, 7.8)

        c.find_relative_position('circle')
    
    assert pytest_wrapped_e.type == SystemExit

def test_no_common_points():
    c1 = Circle(Point(2.0, 1.0), 1.0)
    c2 = Circle(Point(6.0, 4.0), 2.0)
    assert c1.find_relative_position(c2) == RelativePosition.NO_COMMON_POINTS

    c1 = Circle(Point(2.0, 1.0), 9.0)
    c2 = Circle(Point(6.0, 4.0), 20.0)
    assert c1.find_relative_position(c2) == RelativePosition.NO_COMMON_POINTS

def test_touching():
    c1 = Circle(Point(2.0, 1.0), 2.0)
    c2 = Circle(Point(6.0, 4.0), 3.0)
    assert c1.find_relative_position(c2) == RelativePosition.TOUCHING

    c1 = Circle(Point(2.0, 1.0), 16.0)
    c2 = Circle(Point(6.0, 4.0), 21.0)
    assert c1.find_relative_position(c2) == RelativePosition.TOUCHING

def test_intersecting():
    c1 = Circle(Point(2.0, 1.0), 5.0)
    c2 = Circle(Point(6.0, 4.0), 6.0)
    assert c1.find_relative_position(c2) == RelativePosition.INTERSECTING

def test_same():
    c1 = Circle(Point(2.0, 2.0), 5.0)
    c2 = Circle(Point(2.0, 2.0), 5.0)
    assert c1.find_relative_position(c2) == RelativePosition.SAME
