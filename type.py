def power_of_type(*args):
	new_args = list(args)
	print(list(args))
	for x in new_args:
		if(type(x) == type("")):
			print(f"{x}, is a string")
		elif(type(x) == type(0)):
			print(f"{x}, is a number ")
		elif(type(x)== type([])):
			print(f"{x}, is a list")
		else:
			print(f"I don't know anything about, {x} ")
power_of_type(2, 3,4, "hello", [2,2,3], (2,4,5)) 		