class Animal:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
	def display_info(self):
		print(f"my name is {self.name}. And i weigh {self.weight} kg")
		
		
class HigherAnimal(Animal):
	def __init__(self, legs, arms, language):
		super().__init__()
		self.legs = legs
		self.arms = arms
		self.language = language 
		
		
class Human(HigherAnimal):
	pass
hafiz = Human("hafiz", 65, "yoruba", 5,6)
hafiz.display_info()