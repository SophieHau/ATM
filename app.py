from flask import Flask, render_template, redirect, request, url_for
from account import Account

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        a = Account()
        account_number = request.form.get('account_number')
        if a.account_login(account_number, request.form.get('pin')) == True:
            return redirect(url_for('menu', account_number=account_number))
    return render_template('index.html')

@app.route("/menu/<int:account_number>")
def menu(account_number):
    a = Account()
    account = a.get_account(account_number)
    return render_template('menu.html', account=account)

@app.route("/withdrawal/<int:account_number>", methods=['POST', 'GET'])
def withdraw(account_number):
    if request.method == 'POST':
        a = Account()
        amount = request.form.get('amount')
        a.withdraw(amount, account_number)
        return redirect(url_for('menu', account_number=account_number))

    return render_template('withdrawal.html')

@app.route("/deposit/<int:account_number>", methods=['POST', 'GET'])
def deposit(account_number):
    if request.method == 'POST':
        a = Account()
        amount = request.form.get('amount')
        a.deposit(amount, account_number)
        return redirect(url_for('menu', account_number=account_number))

    return render_template('deposit.html')