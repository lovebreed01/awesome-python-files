or_list = [0, 1,2,3,4,5,6, 7,8,9]
def rem():
	while or_list != []:
		for i in or_list:
		 	or_list.remove(or_list[0]) 
		 	print (F"UPDATED LIST {or_list} ")
		 	try :
		 		print(f" \n removed {or_list[0]} ") 
		 	except IndexError:
		 		print('Nothing more in the list! ')
	return(or_list )
rem()