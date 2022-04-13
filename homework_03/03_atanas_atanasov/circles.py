from enum import Enum

class point:
	xcoord = 0
	ycoord = 0

	def __init__(self, x, y):
		self.xcoord = x
		self.ycoord = y

	def toString(self):
		print("x: ", self.xcoord, "\ny: ", self.ycoord)

class circleStates(Enum):
	NO_COMMON_POINTS = 0
	TOUCHING = 1
	INTERSECTING = 2
	SAME = 3		

class circle:
	center = 0
	radius = 0

	def __init__(self, c, r):
		self.center = c
		self.radius = r

	def toString(self):
		print("center coordinates:")
		self.center.toString()
		print("radius: ", self.radius)

	def find_relative_position(self, circle):
		if(self.center.xcoord == circle.center.xcoord and self.center.ycoord == circle.center.ycoord):
			return circleStates.SAME
		
		distSq = (self.center.xcoord - circle.center.xcoord) ** 2 + (self.center.ycoord - circle.center.ycoord) ** 2
		radSumSq = (self.radius + circle.radius) ** 2;
		
		if (distSq == radSumSq):
			return circleStates.TOUCHING
		elif (distSq > radSumSq):
			return circleStates.NO_COMMON_POINTS
		elif (distSq < radSumSq):
			return circleStates.INTERSECTING