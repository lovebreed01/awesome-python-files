price = int(input("price : "))
perc = float(input("percentage : ")) 
def calc_perc(price, perc):
	return price * (perc / 100)
t = calc_perc(price, perc)
print(t)