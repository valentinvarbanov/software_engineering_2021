from circle import Circle, Point, RealativePosition

def test_same():
    circle1 = Circle(Point(0.0, 0.0), 5.0)
    circle2 = Circle(Point(0.0, 0.0), 5.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.SAME

def test_intersecting():
    circle1 = Circle(Point(0.0, 0.0), 2.0)
    circle2 = Circle(Point(5.0, 0.0), 5.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.INTERSECTING

def test_touching():
    #outside
    circle1 = Circle(Point(-1.0, 1.0), 3.0)
    circle2 = Circle(Point(3.0, -2.0), 2.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.TOUCHING

    #inside
    circle1 = Circle(Point(-1.0, 0.0), 3.0)
    circle2 = Circle(Point(3.0, -3.0), 8.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.TOUCHING

def test_no_common_points():
    #completly outside
    circle1 = Circle(Point(0.0, 0.0), 3.0)
    circle2 = Circle(Point(5.0, 0.0), 9.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.NO_COMMON_POINTS

    #common ceter
    circle1 = Circle(Point(0.0, 0.0), 3.0)
    circle2 = Circle(Point(0.0, 0.0), 9.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.NO_COMMON_POINTS

    #completly inside
    circle1 = Circle(Point(0.0, 0.0), 9.0)
    circle2 = Circle(Point(1.0, 0.0), 3.0)
    assert circle1.find_relative_position(circle2) == RealativePosition.NO_COMMON_POINTS