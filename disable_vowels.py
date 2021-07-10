def disable(str):
	vowels = ["a", "e", "i", "o", "u"]
	for i in str:
		if i in vowels:
			str = str.replace(i,"*")
	return(str)
	
	