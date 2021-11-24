
from krug import is_in_circle, Position


def test_is_in_circle_inside():
    assert is_in_circle(0,0) == Position.inside
    assert is_in_circle(0.206, 0.9567) == Position.inside
    assert is_in_circle(0.2, 0.6) == Position.inside

def test_is_in_circle_outside():
    assert is_in_circle(2,0) == Position.outside

def test_is_in_circle_on():
    assert is_in_circle(1,0) == Position.on
    assert is_in_circle(0.291, 0.9567) == Position.on
    

    