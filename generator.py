import sqlite3
from random import *
from models import Account




class Generator():
    def __init__(self):
        self.account_number = 0
        self.pin = 0
        self.balance = 0

    def generate_account_number(self):
        for x in range(101):
            self.account_number = randint(100000, 1000000)
        return self.account_number

    def generate_pin(self):
        for x in range(101):
            self.pin = randint(1, 1000)
        return self.pin

    def generate_balance(self):
        for x in range(101):
            self.balance = randint(1, 1000000)
        return self.balance
