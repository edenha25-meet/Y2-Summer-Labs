from flask import Flask, render_template
import random


app = Flask(__name__,
template_folder='templates',
static_folder= 'static')

@app.route('/')
def home():
    return render_template(
"home.html")
@app.route('/fortune')
def fortune():
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
    random_fortune= random.choice(fortunes)
    return render_template('fortune.html', fortune = random_fortune)



if __name__ == '__main__':
    app.run(debug = True)
    