from circle import Circle, Point, RelativePosition

def test_no_common_points():
    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(4.00001, 0.0), 2.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS

    circle_1 = Circle(Point(1.0, 2.0), 2.97)
    circle_2 = Circle(Point(5.0, 4.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS

    circle_1 = Circle(Point(-3.0, 2.0), 2.3)
    circle_2 = Circle(Point(5.0, -1.0), 1.8)

    assert circle_1.circle_position(circle_2) == RelativePosition.NO_COMMON_POINTS      

def test_touching():
    circle_1 = Circle(Point(-2.0, 0.0), 2.0)
    circle_2 = Circle(Point(2.0, 0.0), 2.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.TOUCHING

    circle_1 = Circle(Point(0.0, 1.5), 2.5)
    circle_2 = Circle(Point(0.0, -1.5), 0.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.TOUCHING

def test_intersecting():
    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(3.0, 0.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

    circle_1 = Circle(Point(1.0, 2.0), 3.0)
    circle_2 = Circle(Point(-1.0, -3.0), 5.0)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

    circle_1 = Circle(Point(-3.0, 2.0), 2.2)
    circle_2 = Circle(Point(-4.0, -1.0), 4.4)

    assert circle_1.circle_position(circle_2) == RelativePosition.INTERSECTING

def test_same():
    circle_1 = Circle(Point(0.0, 0.0), 2.0)
    circle_2 = Circle(Point(0.0, 0.0), 1.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME

    circle_1 = Circle(Point(1.0, 1.0), 3.0)
    circle_2 = Circle(Point(1.5, 1.0), 2.5)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME

    circle_1 = Circle(Point(-2.0, -2.0), 5.0)
    circle_2 = Circle(Point(-1.0, -1.0), 1.8)

    assert circle_1.circle_position(circle_2) == RelativePosition.SAME           