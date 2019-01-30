def odd_numbers():
	
	"Returns odd numbers of the input"""
	
	
	x = int(input())
	if x == 0:
		print(x)
	elif x % 2 == 1:
		print(x)
		odd_numbers()
	elif x % 2 == 0:
		odd_numbers()
			
		

