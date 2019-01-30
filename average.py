def average(sum = 0, number = 0):
	""" Function returns average of input values"""
	
	x = int(input())
	if x == 0:
		return (sum / number, number)
	else:
		return(average(sum + x, number + 1))
		
		

	