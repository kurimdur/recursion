def exponent_of_2(number):
	
	"""Returns 'yes' if number is exponent of 2"""
	
	
	if number == 0:
		print("NO")
	elif number == 1:
		print("YES")	
	elif number % 2 == 0:
		exponent_of_2(number / 2)
	else:
		print("NO")
		