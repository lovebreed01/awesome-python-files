class Parser:
	def __init__(self, file):
		self.file = file
		self.data = None
	def parse(self):
		import json 
		with open(self.file) as myfile:
			if myfile.name.endswith(".json"):
				self.data = json.load(myfile)
				return self.data
	def parse_add_data(self, **kwargs):
		import json 
		with open(self.file) as dfile:
			if dfile.name.endswith(". json"):
				self.data = json.load(myfile)
			new_data = []
			new_data.append(kwargs)
			self.data = self.data.extend(new_data) 
		return self.data

p = Parser("test.json") 
p=p.parse_add_data(name="hello")
print(p)