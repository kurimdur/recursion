def usual_order(number):
	
	"""Return prints each digit of the number in separate line"""
	
	if number // 10 < 10:
		print (number // 10)
		print(number % 10)
	else:
		usual_order(number // 10)
		print(number % 10)
	
	

usual_order(45775826)