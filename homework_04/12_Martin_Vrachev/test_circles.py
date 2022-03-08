'''
Unit tests for circles.py
'''

import pytest
from circles import distance, Point, Circle, RelativePosition

def test_create_point():
    '''
    Tests for point creation
    '''
    point_1 = Point(5.4, 6.5)
    assert isinstance(point_1, Point)

def test_create_invalid_point():
    '''
    Tests for creating invalid point
    '''
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        Point('koko', 5.7)

    assert pytest_wrapped_e.type == SystemExit

def test_create_circle():
    '''
    Tests circle creation
    '''
    point_1 = Point(5.5, 4.5)
    circle_1 = Circle(point_1, 10.0)
    assert isinstance(circle_1, Circle)

def test_create_invalid_circle():
    '''
    Tests for creating invalid circles
    '''
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        Circle(5, 6.7)

    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        point_1 = Point(1.2, 8.7)
        Circle(point_1, 'radius')

    assert pytest_wrapped_e.type == SystemExit

def test_distance():
    '''
    Tests for distance between two points
    '''
    point_1 = Point(2.0, 1.0)
    point_2 = Point(6.0, 4.0)
    assert distance(point_1, point_2) == 5.0

    point_1 = Point(2.0, -1.0)
    point_2 = Point(-2.0, 2.0)
    assert distance(point_1, point_2) == 5.0

def test_invalid_distance_arguments():
    '''
    Tests for invalid araguments
    '''
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        distance(2,3)

    assert pytest_wrapped_e.type == SystemExit

def test_find_realtive_position_invalid_arguments():
    '''
    Tests for invalid araguments
    '''
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        point_1 = Point(5.6, 1.2)
        circle_1 = Circle(point_1, 7.8)

        circle_1.find_relative_position('circle')

    assert pytest_wrapped_e.type == SystemExit

def test_no_common_points():
    '''
    Tests if two circles have common points
    '''
    circle_1 = Circle(Point(2.0, 1.0), 1.0)
    circle_2 = Circle(Point(6.0, 4.0), 2.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.NO_COMMON_POINTS

    circle_1 = Circle(Point(2.0, 1.0), 9.0)
    circle_2 = Circle(Point(6.0, 4.0), 20.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.NO_COMMON_POINTS

def test_touching():
    '''
    Tests if two cricles are touching
    '''
    circle_1 = Circle(Point(2.0, 1.0), 2.0)
    circle_2 = Circle(Point(6.0, 4.0), 3.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.TOUCHING

    circle_1 = Circle(Point(2.0, 1.0), 16.0)
    circle_2 = Circle(Point(6.0, 4.0), 21.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.TOUCHING

def test_intersecting():
    '''
    Tests if two cricles are intersecting
    '''
    circle_1 = Circle(Point(2.0, 1.0), 5.0)
    circle_2 = Circle(Point(6.0, 4.0), 6.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.INTERSECTING

def test_same():
    '''
    Tests if two cricles are same
    '''
    circle_1 = Circle(Point(2.0, 2.0), 5.0)
    circle_2 = Circle(Point(2.0, 2.0), 5.0)
    assert circle_1.find_relative_position(circle_2) == RelativePosition.SAME
