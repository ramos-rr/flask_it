# Class 4 - URL build up

# Start up importing two more functions: "redirect" and "url_for"
from flask import Flask, redirect, url_for

app = Flask(__name__)


# Mock an admin page
@app.route("/admin/")
def admin():
    return f"<h1>Admin</h1>"


# Mock a page to be redirected
@app.route("/guest/<name>")
def guest(name):
    return f"<p>Hello guest {name}</p>"


# Now, stablish route rules
# It looks like the "add.url_rule" seen before in class 2.
@app.route("/user/")
@app.route("/user/<name>")
def user(name=""):
    if name == "admin":
        return redirect(url_for('admin'))
    elif name == "":
        return "<p>You need to type a name as parameter</p>", 404
    else:
        return redirect(url_for("guest", name=name))


# Let's redirect to goole's page
@app.route("/google/")
def go_goole():
    return redirect("http://google.com")


if __name__ == '__main__':
    app.run(debug=True, port=4000)

