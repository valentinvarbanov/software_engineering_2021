import main_task
import math 

# simple test if we can create a point
def create_point():
    point = main_task.Point(1, 2)
    assert isinstance(point, main_task.Point)

# simple test if we can create a circle
def create_circle():
    center = main_task.Point(3 ,6)
    r = 2
    circle = main_task.Circle(center, r)
    assert isinstance(circle, main_task.Circle)

# test if one circle is on the same place like the other (in this case i use the same circle)
def test_same_circles():
    circle1 = main_task.Circle(main_task.Point(1.0, 2.0), 1.0)

    assert circle1.find_relative_position(circle1) == main_task.ReturnTypes.SAME

# test if there are not any common points
def test_no_common_points():
    circle1 = main_task.Circle(main_task.Point(0.0, 0.0), 1.0)
    circle2 = main_task.Circle(main_task.Point(5.0, 5.0), 1.0)

    assert circle1.find_relative_position(circle2) == main_task.ReturnTypes.NO_COMMON_POINTS

# test if circles are touching each other - externally and internally
def test_touching():
    # externally
    circle1 = main_task.Circle(main_task.Point(1.0, 1.0), 3.0)
    circle2 = main_task.Circle(main_task.Point(5.0, 4.0), 2.0)

    assert circle1.find_relative_position(circle2) == main_task.ReturnTypes.TOUCHING

    # internally
    circle3 = main_task.Circle(main_task.Point(0.0, 0.0), 1.0)
    circle4 = main_task.Circle(main_task.Point(5.0, 0.0), 6.0)

    assert circle3.find_relative_position(circle4) == main_task.ReturnTypes.TOUCHING

# test if cirlces are intersecting each other
def test_intersecting():
    circle1 = main_task.Circle(main_task.Point(1.0, 1.0), 1.0)
    circle2 = main_task.Circle(main_task.Point(1.5, 1.0), 1.0)

    assert circle1.find_relative_position(circle2) == main_task.ReturnTypes.INTERSECTING