def is_prime(number, divider = 2):
	
	"""Returns 'YES' if number is prime, or 'NO' if not"""
	
	
	if number == 1 or 0:
		return"NO"
	elif number == 2:
		return "YES"
	elif number %  divider == 0:
		return "NO"
	elif (divider < number / 2):
		return is_prime(number, divider + 1)
	else:
		return "YES"

