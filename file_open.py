book = open("booker.html", "r+")
str = "\nThis is the first time I've ever seen a black diamond in the world \n I will love to hold you down here "
book.write(str)
for words in book :
	print(words)