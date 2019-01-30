def number_of_ones():
	
	"Returns set of the ones from the input"""
	
	x = int(input())
	y = int(input())
	if x == 0 and y == 0:
		return (0, 0)
	elif y == 0 and x != 0:
		z = int(input())
		if z == 0:
			return (x, y)
		else:
			ones = number_of_ones()
			answer = (x, z, y) + ones
			return tuple(filter(lambda x: x == 1, answer))
	else:
		ones = number_of_ones()
		answer = (x, y) + ones
		return tuple(filter(lambda x: x == 1, answer))
	

		