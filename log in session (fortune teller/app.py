from flask import Flask, render_template, request, redirect, url_for
import random
from flask import session as login_session

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'clifforddddd'  

fortunes = [
    "Opportunity knocks softly, listen carefully.",
    "A thrilling adventure awaits you just around the corner.",
    "Your kindness will lead you to unexpected happiness.",
    "Good things come to those who wait patiently.",
    "A new romantic interest will bring joy into your life.",
    "Embrace change with courage; it will bring you great rewards.",
    "Your creativity will soon bring you financial success.",
    "A long-lost friend will reconnect with you in the near future.",
    "Your hard work will pay off beyond your expectations.",
    "Unexpected travel will bring you great experiences and memories."
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login_session["birthmonth"] = request.form["birthmonth"]
        login_session["username"] = request.form["username"]
        return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    username = login_session.get("username")
    return render_template('home.html', username=username)

@app.route('/fortune')
def fortune():
    birthmonth = login_session.get("birthmonth")
    month_length = len(birthmonth)
    if month_length <= len(fortunes):
        random_fortune = fortunes[month_length - 1] ## '-1' so there isnt an outofbound error
    else:
        random_fortune = "Your birth month is too long for a fortune."

    return render_template('fortune.html', fortune=random_fortune)

@app.route('/indecisive')
def indecisive():
    indecisive_fortunes = [random.choice(fortunes) for i in range(3)]
    return render_template('indecisive.html', indecisive_f=indecisive_fortunes)

if __name__ == '__main__':
    app.run(debug=True)
