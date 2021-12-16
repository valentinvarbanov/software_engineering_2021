from math import sqrt, pow
from Point import Point
from RelativePosition import RelativePosition

class Circle:
    def __init__(self, input_center_point, input_radius):
        self.set_radius(input_radius)
        self.set_center_point(input_center_point)

    def radius(self):
        return self.__radius

    def center_point(self):
        return self.__center_point

    def set_radius(self, radius):
        if isinstance(radius, float) != True:
            raise ValueError("Radius should be of type float")
        if radius < 0:
            raise ValueError("Radius should be a positive integer")
        self.__radius = radius

    def set_center_point(self, center_point):
        if isinstance(center_point, Point) != True:
            raise ValueError("Center_Point should be of type Point")
        self.__center_point = center_point

    def is_center_point_equal(self, other):
        return (self.center_point().x() == other.center_point().x()) and (self.center_point().y() == other.center_point().y())

    def get_position(self, other_circle):
        distance_between_centers = Point.get_distance_between_two_points(self.center_point(), other_circle.center_point())

        collective_radius_difference = abs(self.radius() - other_circle.radius())
        
        collective_radius = abs(self.radius() + other_circle.radius())

        if collective_radius_difference < distance_between_centers and distance_between_centers < collective_radius:
            return RelativePosition.INTERSECTING
            
        if distance_between_centers <= collective_radius_difference or self.is_center_point_equal(other_circle) is True:
            return RelativePosition.SAME

        if distance_between_centers > collective_radius:
            return RelativePosition.NO_COMMON_POINTS

        if distance_between_centers == collective_radius:
            return RelativePosition.TOUCHING