# Class 3 - Creating dinamic URLs
from flask import Flask

app = Flask(__name__)


# ROUTE with a variable between "< >" in the decorator
# Than, set a parameter to be shown at screen
# This way, it is necessary to enter the full url to get status 200
@app.route("/hello/<nome>")
def hello(nome):
    return f"<h1> Hello {nome} </h>"


# Now, let's ajust to recieve both cases: "/hi" and "hi/<name>"
@app.route("/hi/")
@app.route("/hi/<name>")
def hi(name=""):
    return f"<h1>Hi {name}</h1>"


# Define a INTEGER to serve as dinamic
@app.route("/blog/")
@app.route('/blog/<int:postID>')
def blog(postID=0):
    if postID > 0:
        return f"Blog info {postID}"
    else:
        return f"Blog todo"


# Use the same logic to get a float as well
@app.route('/blog/<float:postID>')
def blog2(postID):
    if postID > 0:
        return f"Blog float info {postID}"
    else:
        return f"Blog float todo"


if __name__ == '__main__':
    app.run(debug=True, port=3000)
