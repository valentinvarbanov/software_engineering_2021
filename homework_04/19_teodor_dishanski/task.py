"""The file contains the logic of the task from Homework 3."""

from enum import Enum


class RelativePosition(Enum):
    """Enumeration class.

    It contains the values of the possible
    relative positions of two circles.
    """

    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3


class Point:
    """Basic class Point.

    The class define the basic term of a point.
    A point is defined by two coordinates (X, Y)
    in Cartesian coordinate system.
    """

    def __init__(self, x_coordinate, y_coordinate) -> None:
        """Create an instance of type Point.

        Parameters: x_coordinate - float value
                    y_coordinate - float value
        """
        assert isinstance(x_coordinate, float)
        assert isinstance(y_coordinate, float)

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __eq__(self, other_point) -> bool:
        """Return if two points are same."""
        assert isinstance(other_point, Point)
        return self.x_coordinate == other_point.x_coordinate and \
            self.y_coordinate == other_point.y_coordinate

    def distance(self, other_point) -> float:
        """Return distance between the current point and another one.

        Arguments: other_point - An instance of the class Point

        The distance between two points is calculated using
        the Pytoagorean theorem (a^2 + b^2 = c^2).
        """
        assert isinstance(other_point, Point)
        result_x = self.x_coordinate - other_point.x_coordinate
        result_y = self.y_coordinate - other_point.y_coordinate
        return (result_x ** 2 + result_y ** 2) ** 0.5


class Circle:
    """Basic class Circle.

    The class define the basic term of a circle.
    A circle is defined by a center point and a
    positive value of a radius.
    """

    def __init__(self, center, radius) -> None:
        """Create an instance of type Circle.

        Parameters: center - Point instance
                    radius - poistive float value
        """
        assert isinstance(center, Point)
        assert isinstance(radius, float)
        assert radius > 0

        self.center = center
        self.radius = radius

    def __eq__(self, other_circle) -> bool:
        """Return if two circles are same."""
        assert isinstance(other_circle, Circle)
        return self.center == other_circle.center and \
            self.radius == other_circle.radius

    def find_relative_position(self, other_circle) -> RelativePosition:
        """Return the relative position of the current cicle and another.

        Arguments: other_circle - An instance of the class Circle

        The decision of the relative position between 2 circles
        can be found in the folder Homework 3.
        """
        assert isinstance(other_circle, Circle)

        distance_centers = self.center.distance(other_circle.center)
        radii_sum = self.radius + other_circle.radius
        radii_diff = abs(self.radius - other_circle.radius)

        if self == other_circle:
            return RelativePosition.SAME

        condition1 = abs(distance_centers - radii_sum) < 0.001
        condition2 = abs(distance_centers - radii_diff) < 0.001

        if condition1 or condition2:
            return RelativePosition.TOUCHING

        if distance_centers > radii_sum or distance_centers < radii_diff:
            return RelativePosition.NO_COMMON_POINTS

        return RelativePosition.INTERSECTING
