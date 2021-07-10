import time

t = time.localtime(time.time())
format = time.strftime("%H : %M : %S", t)
print(format) 