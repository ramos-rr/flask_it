# Class 11 - Cookies
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/setcookie", methods=['POST', "GET"])
def setcookie():
    resp = make_response(render_template('setcookie.html'))

    if request.method == "POST":
        data = request.form['cookie']
        resp.set_cookie('testCookie', data)

    return resp


@app.route('/getcookie')
def getcookie():
    cookie_name = request.cookies.get("testCookie")
    return f'<h1>Cookie value: {cookie_name}'


if __name__ == '__main__':
    app.run(debug=True, port=11000)
