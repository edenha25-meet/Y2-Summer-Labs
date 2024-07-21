from flask import Flask, render_template, request, redirect, url_for, session as login_session

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'clifforddddd'  

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login_session["password"] = request.form["password"]
        login_session["username"] = request.form["username"]
        return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    username = login_session.get("username")
    return render_template('home.html', username=username)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
