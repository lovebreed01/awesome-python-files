import random
maxn = 10
n = random.randint(1, maxn)
guess_count =0
out_of_guess= False
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None
while guess != n and guess_count < 5:
    guess = int(input('Your try: '))
    guess_count += 1
    if guess > n:
        print('Too high')
    if guess < n:
        print('Too low')
    if guess_count >= 5:
    	out_of_guess= True
    	print("You lost the game")
    	break
    print("Congratulations ")


print("You guess the number %d " %guess_count )
