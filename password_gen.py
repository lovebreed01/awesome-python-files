import random as r
letters = ["a","m","x","p","q","l","r","t","f","g"]
digits=[0,1,2,3,4,5,6,7,8,9]
chars=["$","&","#","/","@","?","%","¿","*","+"]
def gen_pass():
	p1=r.choice(letters)
	p2=r.choice(str(digits))
	p3=r.choice(chars)
	p4=r.choice(str(digits))
	p5=r.choice(chars)
	p6=r.choice(letters)
	p7=r.choice(chars)
	p8=r.choice(letters)
	password=p1 + p2 + p3 + p4 + p5 + p6 + p7 +p8
	print(str(password))
gen_pass()