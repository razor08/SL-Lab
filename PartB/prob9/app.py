from flask import Flask, redirect, render_template, request, url_for
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            # time.strptime(request.form["dob"],"%d%m%Y")
            time.strptime(request.form["dob"],"%d/%m/%Y")
        except:
            msg="You entered an invalid date. This response is from server side!"
            return render_template('index.html', msg=msg)

        return render_template('success.html')

if __name__ == '__main__':
    app.run()