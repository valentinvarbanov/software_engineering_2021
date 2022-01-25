from circles import point, circle, circleStates

def test_inside():
	print("Begin intersecting circles test")

	p1 = point(3, 4)
	p2 = point(5, 3)
	p3 = point(6, 6)

	c1 = circle(p1, 1.5)
	c2 = circle(p2, 1.25)
	c3 = circle(p3, 3)

	assert c1.find_relative_position(c2) == circleStates.INTERSECTING
	assert c2.find_relative_position(c3) == circleStates.INTERSECTING
	assert c3.find_relative_position(c1) == circleStates.INTERSECTING

	print("Test successful\n")

def test_touching():
	print("Begin touching circles test")

	p1 = point(1, 0.5)
	p2 = point(3, 0.5)
	p3 = point(1, 2.5)

	c1 = circle(p1, 1)
	c2 = circle(p2, 1)
	c3 = circle(p3, 1)

	assert c1.find_relative_position(c2) == circleStates.TOUCHING
	assert c3.find_relative_position(c1) == circleStates.TOUCHING

	print("Test successful\n")

def test_noCommonPoints():
	print("Begin no common points test")

	p1 = point(3, 0.5)
	p2 = point(1, 2.5)
	p3 = point(6, 6)

	c1 = circle(p1, 1)
	c2 = circle(p2, 1)
	c3 = circle(p3, 3)

	assert c1.find_relative_position(c2) == circleStates.NO_COMMON_POINTS
	assert c2.find_relative_position(c3) == circleStates.NO_COMMON_POINTS
	assert c3.find_relative_position(c1) == circleStates.NO_COMMON_POINTS

	print("Test successful\n")
	
def test_same():
	print("Begin common center test")

	p1 = point(3, 4)
	p2 = point(5, 3)

	c1 = circle(p1, 1.5)
	c2 = circle(p2, 1.25)
	c3 = circle(p1, 2)
	c4 = circle(p2, 3)

	assert c1.find_relative_position(c3) == circleStates.SAME
	assert c2.find_relative_position(c4) == circleStates.SAME

	print("Test successful")

print("Testing find_relative_position() function\n")
test_inside()
test_touching()
test_noCommonPoints()
test_same()