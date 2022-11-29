# Class 10 - Sending data from templates
from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__, template_folder='templates')


# Let's recieve some NOTE from students and print them
@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/")
def index():
    return redirect(url_for("notes"), 302)


@app.route("/calculate", methods=["POST"])
def calculate():
    notes = dict()
    total = sum([int(v) for v in request.form.to_dict().values()])
    notes["sum"] = total
    notes["average"] = total/4
    return render_template('calculate.html', notes=notes)


if __name__ == '__main__':
    app.run(debug=True, port=10000)
