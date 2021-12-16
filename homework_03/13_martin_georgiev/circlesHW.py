import enum

class RelativePosition (enum.Enum):
    NO_COMMON_POINTS = 0
    TOUCHING = 1
    INTERSECTING = 2
    SAME = 3

class Point:
    def __init__(self, x, y):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        self.x = x
        self.y = y

class Circle:
    def __init__(self, O, r):
        assert isinstance(r, (int, float))
        assert isinstance(O, Point)
        self.O = O
        self.r = r

    def find_relative_position(self, circle2):

        assert isinstance(circle2, (Circle ))

        distance = ((((self.O.x - circle2.O.x )**2) + ((self.O.y - circle2.O.y)**2) )**0.5)

        if self.r > circle2.r:
            big_r = self.r
            small_r = circle2.r
        else:
            small_r = self.r
            big_r = circle2.r

        # if distance > self.r + circle2.r
        if distance - (self.r + circle2.r) > 0.001:
            return RelativePosition.NO_COMMON_POINTS

        # if distance == self.r + circle2.r
        elif abs(distance - (self.r + circle2.r)) < 0.001:
            return RelativePosition.TOUCHING

        else: # => distance < self.r + circle2.r

            # if big_r >= distance + small_r
            if abs(big_r - (distance + small_r)) < 0.001 or big_r - (distance + small_r) > 0.001:
                return RelativePosition.SAME

            return RelativePosition.INTERSECTING


        