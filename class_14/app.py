# Class 13 - CRUD with Flask and SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

# Import BATABASE Lib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

# DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.sqlite.db'
# Instantiate SQLAlchemy
db = SQLAlchemy(app)


# Create class that inherits "db.Models" instantiated above
class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Code
@app.route('/', methods=["GET", "POST"])
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        student = Student(name=request.form.get("name"), age=request.form.get("age"))
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'), 302)
    return render_template('add.html')


@app.route('/edit/student_<int:user_id>', methods=["GET", "POST"])
def edit(user_id):
    query = Student.query.get(user_id)
    if request.method == "POST":
        new_data = {"name": request.form.get("name"), "age": request.form.get("age")}
        if new_data["name"] != '':
            query.name = new_data["name"]
            db.session.commit()
        if new_data["age"] != '':
            query.age = new_data["age"]
            db.session.commit()
        return redirect(url_for('index'), 302)
    return render_template('edit.html', name=query.name, age=query.age, id=query.id)


@app.route('/delete/student_<int:user_id>', methods=["GET", "POST"])
def delete(user_id):
    query = Student.query.get(user_id)
    if request.method == "POST":
        db.session.delete(query)
        db.session.commit()
        return redirect(url_for('index'), 302)
    return render_template("delete.html", name=query.name, age=query.age, id=query.id)


if __name__ == '__main__':
    # Create DB Table
    # Put APP within its context
    with app.test_request_context():
        db.create_all()
    app.run(debug=True, port=14000)
