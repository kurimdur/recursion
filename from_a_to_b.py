def from_a_to_b(a, b):
	
	"""Prints values from a to b if a > b, or from b to a if otherwise"""
	
	if (a > b):
		print(a)
		from_a_to_b(a - 1, b)
		
	elif (a < b):
		from_a_to_b(a, b - 1)
		print(b)			
	else:
		print(a)
			
			
