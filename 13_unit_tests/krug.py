import enum

class Position(enum.Enum):
    inside = 1
    outside = -1
    on = 0


def is_in_circle(x, y):

    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))


    if x*x + y*y > 1:
        return Position.outside
    if abs(x*x + y*y - 1) < 0.001:
        return Position.on

    return Position.inside


print(is_in_circle(1, 0))
print(is_in_circle(2, 3))
