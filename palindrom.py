def palindrom(word, i):
	
	"""Returns 'YES' if the word is palindrome and 'NO' if not"""
	
	
	if i == (len(word)//2 + 1):
		return("YES")
	elif word[i] == word[len(word) - 1 - i]:
		return(palindrom(word, i + 1))
	else:
		return("NO")


