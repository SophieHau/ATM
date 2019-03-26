from models import Account, db, app
from faker import Faker

fake = Faker()
accounts = Account.query.all()
for account in accounts:
	account.name = fake.name()
	account.credit_card = fake.credit_card_number()
db.session.commit()

