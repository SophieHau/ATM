from account import Account
from generator import Generator

g = Generator()
a = Account()

count = 0
while count < 101:

	account_number = g.generate_account_number()
	pin = g.generate_pin()
	balance = g.generate_balance()
	a.add_account(account_number, pin, balance)
	count += 1
