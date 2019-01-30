def right_to_left(number):
	
	""" Prints the number in reversed order"""
	if number < 10:
		print(number)
	else:
		print(number % 10,end = '')
		right_to_left(number // 10)
		
