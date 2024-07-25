from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = "*******"

firebaseConfig = {
    "apiKey": "AIzaSyCs9MBrMkVxO8-tHpiH8Xz_qcbvRqBhv9Q",
    "authDomain": "w2e-authentication.firebaseapp.com",
    "projectId": "w2e-authentication",
    "storageBucket": "w2e-authentication.appspot.com",
    "messagingSenderId": "128380619254",
    "appId": "1:128380619254:web:464852c478c1c3a3fc1fd7",
    "measurementId": "G-CQXS0B4NFF",
    "databaseURL": "https://w2e-authentication-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:  # if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Womp it failed sad"
            print(error)
            return render_template("signup.html", error=error)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        email = request.form['email']
        password = request.form['password']
        try:
            session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Womp it failed. Try again"
            return render_template("login.html", error=error)

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        db.child("fans").push({"name": name, "email": email, "message": message})
        return redirect(url_for('thanks_page'))
    
    fan_messages = db.child("fans").get().val() or {}
    return render_template('contact.html', fan_messages=fan_messages)

@app.route('/thanks')
def thanks_page():
    return render_template('thanks.html')

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('login'))

@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
