import datetime
import time as t
c = 0

while c < 5:
	time = datetime.datetime. now()
	if time.minute < 10:
		print(f"{time.hour - 12} - 0{time.				minute} - {time.second}..... ")
	else:
		print(f"{time.hour - 12} - {time.				minute} - {time.second}..... ")
	c +=1
	t. sleep(1)
		