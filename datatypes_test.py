l1 = [1,2,3,4]
l2 = ["hello","world","today","now"]
c = dict(zip(l1,l2))
print(c)
for key , value in c.items():
	print(key,value)