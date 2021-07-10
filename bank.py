import sys
class BankUser :
	#users count variable
	bank_user_count = 0 
	
	#constructor function
	def __init__(self, name, acct_num, password, acct_bal, *args, **kwargs):
		self.name = name
		self.acct_num = acct_num
		self.password = password
		self.acct_bal = acct_bal
		BankUser.bank_user_count +=1
	def __str__(self):
		return self.name
		
	#password checker function for the user object 
	def password_check(self):
		password_count=0
		password = None
		too_much_input = False
		while password != self.password and not(too_much_input) :
			password = int(input("Enter your password : ")) 
			password_count +=1
			if password_count > 3:
				too_much_input = True
				if too_much_input:
					print("try again later.........) :")
					sys.exit()
	
	#function that checks the user's account balance
	def balance(self):
		BankUser.password_check(self)
		print("Name : %s \nAccount Number : %d \nBalance : %d  \n................ "%(self.name,self.acct_num, self.acct_bal ))
		
	# function to deposit
	def deposit(self):
		BankUser.password_check(self)
		amount_to_deposit = int(input("Deposit amount in naira : "))
		new_amt = self.acct_bal +  amount_to_deposit 
		self.acct_bal = new_amt
		print("Name : %s \nAccount Number : %d \nBalance : %d  \n...................\n.................. "%(self.name,self.acct_num, self.acct_bal ))
	
	# function to change password 
	def change_pass(self):
		BankUser.password_check(self)
		new_password = int(input("Enter a new passw"))
		self.password= new_password
		
	#function  to withdraw 
	def withdraw(self):
		BankUser.password_check(self)
		amt_to_withdraw = int(input(" Amount to withdraw : "))
		if amt_to_withdraw > self.acct_bal :
			print(" \tInsufficient balance in your account \n........... .......... ")
		else :
			self.acct_bal = self.acct_bal - amt_to_withdraw
			print("You withdrew %d from your account \nYour remaining balance is %d"%(amt_to_withdraw,self.acct_bal))
