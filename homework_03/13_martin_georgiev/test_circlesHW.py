from circlesHW import RelativePosition, Point, Circle

def test_is_circle():
    assert isinstance(Circle(Point(1, 1), 1), Circle)
    assert isinstance(Circle(Point(1.456, 1.234), 0.23), Circle)

    try:
        # wrong input so this should trow error if the code works correctly
        assert not isinstance(Circle(Point("eee", 1), 1), Circle)
    except:
        pass
    
    try:
         # wrong input so this should trow error if the code works correctly
        assert not isinstance(Circle(Point(1, 1), "uuu"), Circle)
    except:
        pass

    try:
         # wrong input so this should trow error if the code works correctly
        assert not isinstance(Circle("ddd", 1), Circle)
    except:
        pass

def test_is_outside():
    # all integers
    assert Circle(Point(1, 1), 1).find_relative_position(Circle(Point(4, 4), 1)) == RelativePosition.NO_COMMON_POINTS
    # secont is float
    assert Circle(Point(1, 1), 1).find_relative_position(Circle(Point(4.123, 4.654), 1.456)) == RelativePosition.NO_COMMON_POINTS
    # all float
    assert Circle(Point(1.12, 1.16), 1.21).find_relative_position(Circle(Point(4.123, 4.654), 1.456)) == RelativePosition.NO_COMMON_POINTS
    # big numbers
    assert Circle(Point(1120, 1160), 1210).find_relative_position(Circle(Point(4123, 4654), 1456)) == RelativePosition.NO_COMMON_POINTS

def test_is_touching():
    # all integers
    assert Circle(Point(1,1), 1).find_relative_position(Circle(Point(1, 3), 1)) == RelativePosition.TOUCHING
    # second is float
    assert Circle(Point(1,1), 1).find_relative_position(Circle(Point(3.56, 2.89), 2.182)) == RelativePosition.TOUCHING
    # all float
    assert Circle(Point(1.12, 1.13), 1.14).find_relative_position(Circle(Point(3.68, 3.02), 2.042)) == RelativePosition.TOUCHING

def test_is_intersecting_not_fully():
    # all integers / the centre of the first circle steps on the second circle and vice versa 
    assert Circle(Point(1, 1), 1).find_relative_position(Circle(Point(1, 2), 1)) == RelativePosition.INTERSECTING
    # second is float / 0 overlapping centres
    assert Circle(Point(1, 1), 1).find_relative_position(Circle(Point(1.456, 2.123), 0.89)) == RelativePosition.INTERSECTING
    # all float / 1 overlapping centre
    assert Circle(Point(1.12, 1.13), 1.456).find_relative_position(Circle(Point(1.456, 2.123), 0.89)) == RelativePosition.INTERSECTING
    # all float / 2 overlapping centres
    assert Circle(Point(1.12, 1.13), 1.456).find_relative_position(Circle(Point(1.456, 2.123), 0.89)) == RelativePosition.INTERSECTING
     # big numbers
    assert Circle(Point(1120, 1130), 1456).find_relative_position(Circle(Point(1456, 2123), 890)) == RelativePosition.INTERSECTING
    
def test_is_same():
    # wrong
    assert not Circle(Point(1, 1), 1).find_relative_position(Circle(Point(1, 2), 1)) == RelativePosition.SAME
    # all integers / one overlapping centre
    assert Circle(Point(1, 1), 3).find_relative_position(Circle(Point(1, 2), 1)) == RelativePosition.SAME
    # second is float / 2 overlapping centres
    assert Circle(Point(1, 1), 3).find_relative_position(Circle(Point(1.456, 2.123), 1.567)) == RelativePosition.SAME
    # all float
    assert Circle(Point(1.12, 1.13), 2.678).find_relative_position(Circle(Point(1.456, 2.123), 1.123)) == RelativePosition.SAME
    # the centre of the first circle steps on the second circle and vice versa 
    assert Circle(Point(1, 1), 2).find_relative_position(Circle(Point(2, 1), 1)) == RelativePosition.SAME
    # big numbers
    assert Circle(Point(1000, 1000), 2000).find_relative_position(Circle(Point(2000, 1000), 1000)) == RelativePosition.SAME