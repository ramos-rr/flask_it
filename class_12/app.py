# Class 12 - SESSION
# Import SESSION function
from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

# SET UP A SECRET KEY
# IT IS RECOMMENDED TO USE AN MORE PROFESSIONAL KEY FROM SPECIALIZED LIBRARIES
app.secret_key = '123456'


# Code
@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session["username"]
    return render_template("index.html", username=username)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form["username"] != "":
        session["username"] = request.form["username"]
        return redirect(url_for('index'), 302)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'), 302)


if __name__ == '__main__':
    app.run(debug=True, port=12000)
