import string
def add_it_up(num):
	if type(num)!= type(0):
		return 0
	elif num < 1:
		print("too small...... ")
		return 0
		
	else:
		total = 0
		for i in range(0,num):
			total += i
		return total 
letters = "hello world"
letters = letters. encode()
#print(type(letters)) 
#print(string.ascii_lowercase[5:] + string.ascii_lowercase[:5])
#print(dir(str)) 
#transtab = str.maketrans( "aeiou", "*****")
#s = "This is fucking serious"
#print(s.translate(transtab))
# caesar.py
import string

def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    print(mask)
    trantab = str.maketrans(letters, mask)
    return plain_text. translate(trantab)
print(caesar("abc"))
