def number_of_max():
	"Returns set of maximum numbers in from the input"""
	
	x = int(input())
	if x != 0:
		y = int(input())
		if y != 0:
			second = number_of_max()
			answer = (x, y) + second
			finish = answer.count(max(answer))
			return tuple(sorted(list(answer), reverse = True))[:finish]
		else:
			return (x, 0)
	else:
		return (0, 0)
	


