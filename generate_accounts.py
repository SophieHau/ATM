from models import Account, db, app
import random
from faker import Faker
# Create a script to generate 1,000 accounts
# Each account has a 6 digits account number
# 3 digits PIN
# a balance between 0 and 10,000

def fake_account_number():
	account_number = random.randint(100000, 999999)
	while Account.query.filter_by(account_number=account_number).first() != None:
		account_number = random.randint(100000, 999999)
	return account_number


def fake_pin():
	return random.randint(100, 999)

def fake_balance():
	return random.randint(0, 10000)

def fake_account():
	return Account(account_number=fake_account_number(), pin=fake_pin(), balance=fake_balance())

def generate_accounts(max_n):
	for n in range(max_n):
		account = fake_account()
		db.session.add(account)

	db.session.commit()	

def add_fake_names():
	fake = Faker()
	accounts = Account.query.all()
	for account in accounts:
		account.name = fake.name()
	db.session.commit()


# count = 0
# while count < 1000:
# 	account_number = randint(100000, 999999)
# 	pin = randint(100, 999)
# 	balance = randint(0, 10000)
# 	account = Account(account_number=account_number, pin=pin, balance=balance)
# 	db.session.add(account)
# 	count += 1
# db.session.commit()

# for n in range(1000):

	# account_number = g.generate_account_number()
	# pin = g.generate_pin()
	# balance = g.generate_balance()
	# a.add_account(account_number, pin, balance)



