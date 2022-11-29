# Class 8 - Redirect and erros
from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)


# Let's use a login page as example
# Don't forget to user status 302 as a redirection success
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form["username"] == 'admin' and request.form["password"] == 'admin':
            return redirect(url_for('home'), code=302)
        else:
            abort(401)
    else:
        abort(403)

    return


@app.route('/home')
def home():
    return "<h1>Bem vindo à área logada</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
