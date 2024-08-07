from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="*******"

firebaseConfig = {
    "apiKey": "AIzaSyCIY7LeeMaup6NGBpRsvmgaopDDJQqHd-M",
    "authDomain": "authentication-60232.firebaseapp.com",
    "projectId": "authentication-60232",
    "storageBucket": "authentication-60232.appspot.com",
    "messagingSenderId": "800914022908",
    "appId": "1:800914022908:web:b4cc4f73ae34fd10a85279",
    "measurementId": "G-PKVPCMB8YL",
    "databaseURL": "https://authentication-60232-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("signin.html")
    else: # if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user'] = user
            user_id = user['localId']
            name = request.form.get('name')
            username = request.form.get('username')
            db.child("users").child(user_id).set({
                "name": name,
                "email": email,
                "password": password,
                "username": username,
            })
            return redirect(url_for('home'))
        except:
            error = "Womp it failed sad"
            return render_template("signin.html", error=error)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        fullname = request.form['fullname']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
            return redirect(url_for('home'))
        except:
            error = "Womp it failed. Try again"
            return render_template("signup.html", error=error)

@app.route('/thanks', methods=["GET", "POST"])
def thanks():
    return render_template("thanks.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        quote = request.form['quote']
        said_by = request.form['said_by']
        user = login_session.get('user')
        if user:
            user_id = user['localId']
            quotes = {
                "quote": quote,
                "said_by": said_by,
                "user_id": user_id
            }
            db.child("users").child(user_id).set(quotes)
            return redirect(url_for('thanks'))
        return redirect(url_for('login'))

@app.route('/display', methods=["GET"])
def display():
    quotes = db.child("quotes").get().val()
    return render_template("display.html", quotes=quotes)

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
