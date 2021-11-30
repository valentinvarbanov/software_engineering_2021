from circle import Point, Circle, RelativePostion 

# test for point initialization
def create_point():
    point = Point(3, 2)
    assert isinstance(point, Point)

# test for circle initialization
def create_circle() -> None:
    center = Point(3, 3)
    r = 1
    circle = Circle(center, r)
    assert isinstance(circle, Circle)

def test_same() -> None:

    circle1 = Circle(Point(6.0, 6.0), 6.0)

    assert circle1.find_relative_position(circle1) == RelativePostion.SAME

    # test with another instance
    circle2 = Circle(Point(6.0, 6.0), 6.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.SAME

    circle3 = Circle(Point(6.0, 6.0), 5.0)

    assert circle1.find_relative_position(circle3) != RelativePostion.SAME



def test_no_common_points() -> None:

    circle1 = Circle(Point(0.0, 0.0), 1.0)
    circle2 = Circle(Point(3.0, 3.0), 1.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.NO_COMMON_POINTS

    circle1 = Circle(Point(3.0, -1.0), 1.0)
    circle2 = Circle(Point(5.0, 2.0), 1.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.NO_COMMON_POINTS


def test_touching() -> None:

    # external touch
    circle1 = Circle(Point(3.0, 3.0), 3.0)
    circle2 = Circle(Point(7.0, 6.0), 2.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.TOUCHING

    # internal touch
    circle3 = Circle(Point(0.0, 0.0), 6.0)
    circle4 = Circle(Point(0.0, 3.0), 3.0)

    assert circle3.find_relative_position(circle4) == RelativePostion.TOUCHING

def test_intersecting() -> None:

    circle1 = Circle(Point(1.0, 1.0), 3.0)
    circle2 = Circle(Point(2.0, 1.0), 3.0)

    assert circle1.find_relative_position(circle2) == RelativePostion.INTERSECTING

test_same()
test_no_common_points()
test_touching()
test_intersecting() 