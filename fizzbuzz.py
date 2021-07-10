def fizzbuzz(n):
	for i in range(n):
		if i % 2 == 0:
			i = "fizz"
		else:
			i = "buzz "
		print(i)
fizzbuzz(20)