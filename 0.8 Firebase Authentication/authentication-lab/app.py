from flask import session as login_session 
from flask import Flask
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="*******"


firebaseConfig = {
   "apiKey": "AIzaSyCIY7LeeMaup6NGBpRsvmgaopDDJQqHd-M",
    "authDomain" : "authentication-60232.firebaseapp.com",
    "projectId": "authentication-60232",
    "storageBucket": "authentication-60232.appspot.com",
    "messagingSenderId": "800914022908",
    "appId": "1:800914022908:web:b4cc4f73ae34fd10a85279",
    "measurementId": "G-PKVPCMB8YL",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Womp it failed sad"
            return render_template("login.html", error=error)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            print(login_session['user'])
            print(login_session['user']['localId'])
            return redirect(url_for('home'))
        except:
            error = "Womp it failed. Try again"
            return render_template("signup.html",error=error)
        
    
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)