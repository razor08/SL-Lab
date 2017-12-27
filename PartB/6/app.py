from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'secret'
@app.route("/", methods=["GET", "POST"])
def server():
    try:
        balance = session['balance']
        count = session['count']
    except KeyError:
        balance = 8000
        session['balance'] = balance
        count = 0
        session['count'] = count
    if request.method=="GET":
        return render_template('index.html', balance = balance, trans = count, msg=' ')
    if request.method == "POST":
        if session['count'] == 5:
            session.clear()
            balance = 8000
            count = 0
            return render_template('index.html', balance = balance, trans = count, msg="Transaction Limit was reached.")

        elif request.form['action'] == 'Deposit':
            if int(request.form['amount']) > 10000:
                return render_template('index.html', balance = balance, trans=count, msg='Deposit amount cannot be greater than 10000')
            else:
                session['balance'] = session['balance'] + int(request.form['amount'])
                session['count'] = session['count'] + 1
                return render_template('index.html', balance = session['balance'], trans = session['count'], msg='Deposit Successfull')
        elif request.form['action'] == 'Withdraw':
            if int(request.form['amount']) > 5000:
                return render_template('index.html', balance = balance, trans=count, msg='Withdraw amount cannot be greater than 5000')
            elif int(request.form['amount']) > session['balance']:
                return render_template('index.html', balance = balance, trans=count, msg='Withdraw amount cannot be greater than current balance')
            else:
                session['balance'] = session['balance'] - int(request.form['amount'])
                session['count'] = session['count'] + 1
                return render_template('index.html', balance = session['balance'], trans = session['count'], msg='Withdraw Successfull')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)