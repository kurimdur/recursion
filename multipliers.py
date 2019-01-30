def multipliers(number, divider = 2):
	
	"""Prints the simple miltipliers of the number"""
	
	
	if number / divider == 1:
		print(number, )
	elif number % divider != 0:
		multipliers(number, divider + 1)
	elif number % divider == 0:
		print(divider, end = '*')
		multipliers(number // divider, divider)
		
	