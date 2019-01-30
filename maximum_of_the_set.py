def maximum_of_the_set(maximum = 0):
	
	"""Returns maximum of the input set of the numbers finishing with 0"""
	
	
	x = int(input())
	if x == 0:
		return maximum
	elif x > maximum:
		return(maximum_of_the_set(x))
	else:
		return(maximum_of_the_set(maximum))
	
