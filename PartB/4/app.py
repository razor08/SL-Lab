
from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def server():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == "POST":
        # print('Yopo')
        date = request.form['dob']
        # print('Yopo')
        date = date.split('/')
        # print('Yopo')        
        try:
            datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        except ValueError:
            return render_template('index.html', msg="Date of Birth Not correct")
        marks= []
        marks.append(int(request.form['m1']))
        marks.append(int(request.form['m2']))
        marks.append(int(request.form['m3']))
        marks.append(int(request.form['m4']))
        # marks.append(int(request.form['m5']))
        credit = []
        credit.append(int(request.form['c1']))
        credit.append(int(request.form['c2']))
        credit.append(int(request.form['c3']))
        credit.append(int(request.form['c4']))
        # credit.append(int(request.form['c5']))
        su=0
        t=0
        for i in range (0, len(marks)):
            su = su + marks[i]*credit[i]
            t = t+credit[i]
        gpa = su/t

        if(gpa > 90):
            gpa = "S"
        elif(gpa > 80):
            gpa = "A"
        elif(gpa > 70):
            gpa = "B"
        elif(gpa > 60):
            gpa = "C"
        elif(gpa > 50):
            gpa = "D"
        elif(gpa > 40):
            gpa = "E"
        else:
            gpa = "F"
        print('Yopo')
        return render_template('index.html', msg="GPA: "+gpa+" Submit Successful")

if __name__ == '__main__':
    app.run()