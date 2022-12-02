# Class 6 - HTTP Methods
from flask import Flask, request

app = Flask(__name__, static_folder='public')

# There are basically 6 methods: GET, POST, PUT, DELETE, HEAD, PATCH


# Let's use a LOGIN example, where both GET and POST are used
# INFORM the route which methods you want
@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return "OKK [POST] => Result %s." % request.form["nome"]
    return "OK [GET]"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
