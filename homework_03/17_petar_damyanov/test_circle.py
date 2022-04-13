from circle import Circle, Point, RelativePosition

def test_no_common_points():
    circle1 = Circle(Point(0.0, 0.0), 6.0)
    circle2 = Circle(Point(1.0, 0.0), 2.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS
    
    circle1 = Circle(Point(4.0, 1.0), 1.0)
    circle2 = Circle(Point(4.0, 12.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS

    circle1 = Circle(Point(2.0, 0.0), 1.0)
    circle2 = Circle(Point(2.0, 0.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.NO_COMMON_POINTS

def test_same():
    circle1 = Circle(Point(1.0, 1.0), 2.0)
    circle2 = Circle(Point(1.0, 1.0), 2.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.SAME
    
def test_touching():
    circle1 = Circle(Point(-1.0, 0.0), 3.0)
    circle2 = Circle(Point(3.0, -3.0), 8.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING

    circle1 = Circle(Point(-1.0, 1.0), 3.0)
    circle2 = Circle(Point(3.0, -2.0), 2.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.TOUCHING
    
def test_intersecting():
    circle1 = Circle(Point(0.0, 0.0), 5.0)
    circle2 = Circle(Point(4.0, 0.0), 6.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.INTERSECTING

    circle1 = Circle(Point(7.0, 0.0), 4.0)
    circle2 = Circle(Point(2.0, 0.0), 5.0)
    assert circle1.find_relative_position(circle2) == RelativePosition.INTERSECTING

