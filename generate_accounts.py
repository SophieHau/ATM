from account import Account, db, app
from random import *

# Create a script to generate 1,000 accounts
# Each account has a 6 digits account number
# 3 digits PIN
# a balance between 0 and 10,000

count = 0
while count < 1000:
	account_number = randint(100000, 1000000)
	pin = randint(100, 1000)
	balance = randint(0, 10001)
	account = Account(account_number=account_number, pin=pin, balance=balance)
	db.session.add(account)
	count += 1
db.session.commit()



	# account_number = g.generate_account_number()
	# pin = g.generate_pin()
	# balance = g.generate_balance()
	# a.add_account(account_number, pin, balance)



