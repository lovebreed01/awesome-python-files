# decorator function
def decorator_func(original_func):
	def wrapper_func():
		print("hello world wrapper func")
		return original_func()
	print("next execution")
	return wrapper_func
	
@decorator_func
def my_func():
	print("This is my original function ")
my_func()
