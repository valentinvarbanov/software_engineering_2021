from hw03 import Circle, Point, RelativePosition

def test_same_position():
    circle = Circle(Point(4.5, 3.3), 6.0)
    other_c = Circle(Point(4.5, 3.3), 6.0)
    assert  circle.find_relative_position(other_c) == RelativePosition.SAME

# inside 
def test_same_case2():
    circle = Circle(Point(0.0, 0.0), 6.0)
    other_c = Circle(Point(0.0, 0.0), 1.0)
    assert  circle.find_relative_position(other_c) == RelativePosition.SAME

# inside 
def test_same_case3():
    circle = Circle(Point(0.0, 0.0), 6.0)
    other_c = Circle(Point(-5.0, 0.0), 1.0)
    assert  circle.find_relative_position(other_c) == RelativePosition.SAME

def test_no_common_points():
    circle = Circle(Point(0.0, 0.0), 6.0)
    other_c = Circle(Point(0.0, -9.0), 1.0)
    assert  circle.find_relative_position(other_c) == RelativePosition.NO_COMMON_POINTS

def test_intersecting():
    circle = Circle(Point(0.0, 0.0), 3.0)
    other_c = Circle(Point(2.0, 1.0), 2.0)
    assert  circle.find_relative_position(other_c) == RelativePosition.INTERSECTING


