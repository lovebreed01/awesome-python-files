def guess_number ():
	import random
	guessed = []
	guess = ""
	guesses = 0
	number_to_guess = random.randint(1,10+1)
	out_of_guesses = False
	guess_limit=5
	while guess != number_to_guess and not (out_of_guesses):
		guess = int(input("Enter your guess : "))
		guesses +=1
		guessed.append(guess)
		print("Your guesses  >>>>", guessed)
		if guess < number_to_guess :
			print("Your guess is too low! \n\t Guess higher! ")
		elif  guess > number_to_guess:
			print("Your guess is too high \n\t Guess lower!  ")
		if guesses == guess_limit:
			out_of_guesses = True
			if out_of_guesses :
				print("You failed! ") 
				break
	else:
		print("Congratulations ")
	choice = None
	choice = input("Do you want to play again? (y/n) : ")
	while choice != "n" :
		choice 
		if choice == "y":
			main()
		else:
			break

def main():
	print("""
	1 - Play Game
	0 - Quit
	""")
	choice = None 
	try:
		while choice != 0:
			choice = int(input("Your Choice : "))
			if choice == 1:
				guess_number()
	except ValueError:
		print("Value must be an integer.. ")
	finally:
		main()
main() 