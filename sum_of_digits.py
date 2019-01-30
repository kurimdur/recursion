def suma_of_digits(number):
	
	"""Returns sum of digits of the number"""
	
	if number < 10:
		return number
	else:
		return suma_of_digits(number // 10) + number % 10
	
	
