from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atm.db'
db = SQLAlchemy(app)


# ATM_DB_PATH = 'data/atm.db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    accounts = db.relationship('Account', backref='user', lazy=True)
    

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    pin = db.Column(db.Integer, unique=False, nullable=False)
    balance = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    



    # def __init__(self):
    #     self.connection = sqlite3.connect(ATM_DB_PATH)
    #     self.cursor = self.connection.cursor()

    # def account_login(account_number, pin):
    # #     query = "SELECT * FROM accounts WHERE account_number = ? AND pin = ?"
    # #     self.cursor.execute(query, (account_number, pin))
    #     account = db.select(account_number)
    #     if account.pin == pin:
    #         return True
    #     else:
    #         return False
    #     self.connection.close()

    # def get_account(account_number):
    #     account = Account.query.get(account_number)
    # # #     query = "SELECT account_number, balance FROM accounts WHERE account_number = ?"
    # # #     self.cursor.execute(query, (account_number,))
    # # #     account_tuple = self.cursor.fetchone()
    # # #     account = {
    # # #         'account_number': account_tuple[0],
    # # #         'balance': account_tuple[1]
    # # #     }
    #     return account
    # #     self.connection.close()

    # def withdraw(amount, account_number):
    #     account = Account.get_account(account_number)
    #     new_balance = int(account['balance']) - int(amount)

    #     query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
    #     self.cursor.execute(query, (new_balance, account_number))
    #     self.connection.commit()
    #     self.connection.close()

    # def deposit(self, amount, account_number):
    #     account = self.get_account(account_number)
    #     new_balance = int(account['balance']) + int(amount)
    #     query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
    #     self.cursor.execute(query, (new_balance, account_number))
    #     self.connection.commit()
    #     self.connection.close()

    # def add_account(self, account_number, pin, balance):
    #     query = "INSERT INTO accounts (account_number, pin, balance) VALUES (?, ?, ?)"
    #     self.cursor.execute(query, (account_number, pin, balance))
    #     self.connection.commit()

    # def get_all_accounts(self):
    #     query = "SELECT account_number FROM accounts"
    #     self.cursor.execute(query)
    #     accounts = self.cursor.fetchall()
    #     return accounts


