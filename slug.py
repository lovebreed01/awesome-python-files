
mystr = "hello my world "
arr = [i for i in mystr]
def rem_white_space(x) :
	x = x.split(" ")
	while " " in x:
		x.remove( " ")
	if " " not in x:
		x = "".join(x)
		print(len(x))
		return x
		
def slugify(x, char = "-"):
	import string 
	if type(char) != type(string.punctuation) and char not in string.punctuation:
		char = "-"
		return f"{char}".join(x.split())
	return f"{char}".join(x.split())
word=" this is   not really nice for today"
x = slugify(word)
print(x)