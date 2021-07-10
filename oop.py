class Hotel:
	def __init__(self, name, rooms, location ):
		self.name = name
		self.rooms =  rooms
		self.location = location
	def __str__(self):
		return self.name
	def hotel_details(self):
		print("Hotel Name : %s \n Rooms Available : %d rooms \n Located at  : %s " %(self.name,self.rooms, self.location))
	def change_details(self, name, rooms, location ):
		self.name = name
		self.rooms = rooms
		self.location =location
 
def make_hotel(name, rooms,location) :
	return Hotel(name, rooms, location)
hafiz = make_hotel(" hafiz", 23,"ijebu")
hafiz.hotel_details()