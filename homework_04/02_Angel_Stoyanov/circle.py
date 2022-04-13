"""A module that contains a circle class"""

from point import Point
from relative_position import RelativePosition

class Circle:
    """A simple class that defines a circle"""

    def __init__(self, input_center_point, input_radius):
        self.set_radius(input_radius)
        self.set_center_point(input_center_point)

    def radius(self):
        """A getter method for the radius field"""
        return self.__radius

    def center_point(self):
        """A getter method for the center point field"""
        return self.__center_point

    def set_radius(self, radius):
        """A setter method for the radius field"""
        if isinstance(radius, float) is not True:
            raise ValueError("Radius should be of type float")
        if radius < 0:
            raise ValueError("Radius should be a positive integer")
        self.__radius = radius

    def set_center_point(self, center_point):
        """A setter method for the center point field"""
        if isinstance(center_point, Point) is not True:
            raise ValueError("Center_Point should be of type Point")
        self.__center_point = center_point

    def is_center_point_equal(self, other):
        """A method that checks if a point is equal to another"""
        return (self.center_point().get_x() == other.center_point().get_x()) \
            and (self.center_point().get_y() == other.center_point().get_y())

    def get_position(self, other_circle):
        """A method that returns the relative position of two circles"""
        distance_between_centers = Point.get_distance_between_two_points(self.center_point(), \
            other_circle.center_point())

        collective_radius_difference = abs(self.radius() - other_circle.radius())

        collective_radius = abs(self.radius() + other_circle.radius())

        if collective_radius_difference < distance_between_centers < collective_radius:
            return RelativePosition.INTERSECTING

        if (distance_between_centers <= collective_radius_difference) or \
                (self.is_center_point_equal(other_circle) is True):
            return RelativePosition.SAME

        if distance_between_centers > collective_radius:
            return RelativePosition.NO_COMMON_POINTS

        if distance_between_centers == collective_radius:
            return RelativePosition.TOUCHING

        return None
