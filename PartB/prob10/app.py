from flask import render_template, request, Flask, url_for, redirect, session
import time

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/", methods= ['GET', 'POST'])
def home_page():
    try:
        balance = session["balance"]
        count = session["count"]
    except KeyError:
        count = 0
        session["count"] = count
        balance  = 8000
        session["balance"] = balance
    if request.method == 'GET':
        return render_template('index.html', balance=balance, transactionCount=count)
    
    if request.method == 'POST':
        if session['count'] == 5:
            msg = "Maximum Transaction Limit Reached"
            transactionCount = count
            session.clear()
            return render_template('index.html',msg=msg, transactionCount= transactionCount, balance=balance)
        else:
            if request.form['action'] == 'Withdraw':
                if int(request.form['amount']) > 5000:
                    msg= 'Server Validation: Cannot withdraw amount greater than 5000'
                    return render_template('index.html', msg = msg, transactionCount=count, balance=balance)
                elif int(request.form['amount']) > session['balance']:
                    msg= 'Server Validation: Cannot withdraw amount more than balance'
                    return render_template('index.html', msg=msg, transactionCount=count, balance=balance)
                else:
                    balance = balance - int(request.form['amount'])
                    session['balance'] = balance
                    session['count'] = session['count'] + 1
                    msg2 = 'Money Withdrawn!'
                    transactionCount = session['count']
                    return render_template('index.html', msg2 =msg2,balance=balance, transactionCount=transactionCount)
            else:
                if int(request.form['amount']) > 10000:
                    msg = 'Server Validation: Cannot make a deposit greater than 10000'
                    return render_template('index.html', msg = msg, transactionCount=count, balance=balance)
                else:
                    balance = balance + int(request.form['amount'])
                    session['balance'] = balance
                    session['count'] = session['count'] + 1
                    msg2 = 'Money Deposited!'
                    transactionCount = session['count']
                    return render_template('index.html', msg2 =msg2, balance=balance, transactionCount=transactionCount)

if __name__ == '__main__':
    app.run()