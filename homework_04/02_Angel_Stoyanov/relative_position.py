"""A module that contains a relative position enumeration"""
import enum

class RelativePosition(enum.Enum):
    """An enum that contains typed relative positions"""
    NO_COMMON_POINTS = 1
    TOUCHING = 2
    INTERSECTING = 3
    SAME = 4
