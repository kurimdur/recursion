def second_max():
	
	"""Returns set of first and second maximum numbers of the input finishing with 0"""
	
	x = int(input())
	if x != 0:
		y = int(input())
		if y != 0:
			second = second_max()
			answer = (x, y) + second
			return tuple(sorted(list(answer), reverse = True))[:2]
		else: 
			return(x, 0)
	else:
		return(0, 0)
			
			
	
			
	
