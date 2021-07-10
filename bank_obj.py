import bank
bank_customers=[]

def create_account():
	name = input("Your Name : ")
	password = int(input("Enter a four digit pin : ")) 
	acct_bal = 0
	user = bank.BankUser(name, acct_num, password, acct_bal)
	bank_customers.append(user) 
	print(user.name,user.acct_num, user.acct_bal)
	print(bank_customers)
	return user
choice = None 	
while choice!= 0:
	choice = int(input("Choice : "))
	if choice == 1:
		create_account()
 
		