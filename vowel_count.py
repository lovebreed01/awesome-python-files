def word_input():
	my_word = input("Enter a word to check :")
	my_word.lower()
	list_word = "".join(my_word.split()) 
	return list_word
	
	
def check_word(word):
	import string 
	char_array = string.punctuation
	for char in char_array:
		if char in word:
			word.remove(char)
		return word
		
		
def vowel_count(words):
	total = 0
	vowels =" aeiou"
	for x in words:
		for i in range(len(vowels)):
			if x ==  vowels[i]:
				total += 1
	print(f" You have {total} vowels in your word....... ")
	print(f" And {len(words) - total} consonants in your word... 🤣😂😂")
	print(words)
	w = f"{len(words.split()) }  words available "
	print(w)
	input("\n\nPress enter to exit... ")
	
	
def main():
		your_word = word_input()
		filtered_word = check_word(your_word) 
		vowels = vowel_count(filtered_word)
main()
		
	
	