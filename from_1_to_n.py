def from_1_to_n(n):
	"""Prints number for 1 to n"""
	
	if n == 1:
		print(1)
	else:
		from_1_to_n(n - 1)
		print(n)
	
