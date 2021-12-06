from problem import Point, Circle, RelativePosition

def test_no_common_points():
    circle_1 = Circle(Point(1.0, 4.0), 3.2)
    circle_2 = Circle(Point(8.0, 4.0), 3.3)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.NO_COMMON_POINTS, True)

def test_touching():
    circle_1 = Circle(Point(1.0, 4.0), 3.2)
    circle_2 = Circle(Point(8.0, 4.0), 3.8)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.TOUCHING, True)

def test_intersecting():
    circle_1 = Circle(Point(1.0, 4.0), 5.2)
    circle_2 = Circle(Point(8.0, 4.0), 3.8)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.INTERSECTING, True)

def test_same_touching():
    circle_1 = Circle(Point(1.0, 4.0), 3.2)
    circle_2 = Circle(Point(1.0, 4.0), 4.0)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.SAME, True)

    circle_1 = Circle(Point(1.0, 4.0), 3.2)
    circle_2 = Circle(Point(4.0, 4.0), 7.8)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.SAME, True)

    circle_1 = Circle(Point(1.0, 4.0), 4.8)
    circle_2 = Circle(Point(4.0, 4.0), 7.8)
    assert(circle_1.find_relative_position(circle_2) == RelativePosition.SAME, True)