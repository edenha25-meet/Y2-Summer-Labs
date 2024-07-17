from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

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

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        birth_month = request.form['birthMonth']
        return redirect(url_for('fortune', month=birth_month))

@app.route('/fortune')
def fortune():
    month = request.args.get('month', '')
    month_length = len(month)
    if month_length <= len(fortunes):
            random_fortune = fortunes[month_length - 1]
    else:
            random_fortune = "Your birth month is too long for a fortune."

    return render_template('fortune.html', fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)
