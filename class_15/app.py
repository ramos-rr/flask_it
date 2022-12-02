# Class 15 - REST api part 1
import json

from flask import Flask

# Let's use previous project and transform it in REST

from flask import Flask, request, jsonify, Response
from class_15.models import Student, db
import json

app = Flask(__name__, template_folder='templates')

# DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.sqlite.db'


# Code
@app.route('/', methods=["GET", "POST"])
def index():
    students = Student.query.all()
    result = [student.to_dict() for student in students]
    return jsonify({"status": "success", "data": result}), 200


@app.route("/view/<int:user_id>", methods=["GET"])
def view(user_id):
    result = db.session.execute(f"SELECT * FROM student WHERE id=%s" % user_id).one()
    return Response(response=json.dumps({"status": "success", "data": dict(result)}), content_type="application/json")


@app.route('/add', methods=["POST"])
def add():
    student = Student(name=request.form.get("name"), age=request.form.get("age"))
    db.session.add(student)
    db.session.commit()
    # return jsonify({"status": "success", "data": student.to_dict()})
    return app.response_class(response=json.dumps({"status": "success", "data": student.to_dict()}), status=200,
                              content_type="application/json")


@app.route('/edit/student_<int:user_id>', methods=["PUT", "POST"])
def edit(user_id):
    query = Student.query.get(user_id)
    new_data = {"name": request.form.get("name"), "age": request.form.get("age")}
    if new_data["name"] != '' or new_data["name"] is None:
        query.name = new_data["name"]
        db.session.commit()
    if new_data["age"] != '' or new_data["age"] is None:
        query.age = new_data["age"]
        db.session.commit()
    query = Student.query.get(user_id)
    return jsonify({"status": "success", "data": query.to_dict()}), 200


@app.route('/delete/student_<int:user_id>', methods=["DELETE"])
def delete(user_id):
    query = Student.query.get(user_id)
    db.session.delete(query)
    db.session.commit()
    return jsonify({"staus": "success", "data": ['deleted', query.to_dict()]}), 200


if __name__ == '__main__':
    # Create DB Table
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True, port=15000)
