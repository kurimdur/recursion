def triangle(k):
	
	"""Prints triangle of numbers with side = k"""
	
	if k > 0:
		triangle(k - 1)
		print(k * str(k))
	

		
	