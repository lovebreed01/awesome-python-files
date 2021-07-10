def gen_pass(length):
	import string
	import random
	numbers = string.digits
	alphas = string.ascii_letters
	chars = string.punctuation
	my_pass = []
	p = ""
	while len(my_pass) < length:
		alpha = random.choice(alphas)
		num = random.choice(numbers)
		char = random.choice(chars)
		my_pass.append(alpha)
		my_pass.append(num)
		my_pass.append(char)
		random.shuffle(my_pass)
	for x in my_pass:
		if type(x) == type(0):
			x = str(x)
		p += x
	return p
my_pass = gen_pass(20)
print(my_pass)
print(type(my_pass))
