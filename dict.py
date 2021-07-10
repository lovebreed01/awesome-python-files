pets = {
'pet1' :{
'name' :'cat', 
'age' : 2}, 
'pet2':{'name' :'dog', 
'age' : 3}
}
print(pets["pet1"].values())
for pet, name in pets.items() :
	print(name["name"], name["age"])