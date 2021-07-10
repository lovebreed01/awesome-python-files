price = float(input("Enter an amount : "))
if price < 10000:
	discount=0.019*price
	print("you have saved", discount,"buy more")
elif price > 10000:
	discount=0.029*price
	print ("you have saved ",discount," buy more")