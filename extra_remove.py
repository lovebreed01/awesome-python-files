names = ["hello", "world", "me", "hello", "blue ", "world", "world", "hello"]

def remove_extra(object):
	print (object, " appears ", names.count(object), " times in the list. ") 
	if names.count(object) > 1 :
			names.remove(object)
			names.sort(	)
			print(names)
			print(object, "still appears ", names.count(object), " times")
remove_extra("world")
remove_extra("world")
remove_extra("hello")
			