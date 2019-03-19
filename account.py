import sqlite3

ATM_DB_PATH = 'data/atm.db'

class Account():
    def __init__(self):
        self.connection = sqlite3.connect(ATM_DB_PATH)
        self.cursor = self.connection.cursor()

    def account_login(self, account_number, pin):
        query = "SELECT * FROM accounts WHERE account_number = ? AND pin = ?"
        self.cursor.execute(query, (account_number, pin))
        account = self.cursor.fetchone()
        if account is not None:
            return True
        else:
            return False
        self.connection.close()

    def get_account(self, account_number):
        query = "SELECT account_number, balance FROM accounts WHERE account_number = ?"
        self.cursor.execute(query, (account_number,))
        account_tuple = self.cursor.fetchone()
        account = {
            'account_number': account_tuple[0],
            'balance': account_tuple[1]
        }
        return account
        self.connection.close()

    def withdraw(self, amount, account_number):
        account = self.get_account(account_number)
        new_balance = int(account['balance']) - int(amount)
        query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
        self.cursor.execute(query, (new_balance, account_number))
        self.connection.commit()
        self.connection.close()

    def deposit(self, amount, account_number):
        account = self.get_account(account_number)
        new_balance = int(account['balance']) + int(amount)
        query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
        self.cursor.execute(query, (new_balance, account_number))
        self.connection.commit()
        self.connection.close()





