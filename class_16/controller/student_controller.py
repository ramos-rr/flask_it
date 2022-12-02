from flask import Blueprint, Response, request, jsonify
from ..models import Student, db
import json

student_blueprint = Blueprint("students", __name__)


# Code
@student_blueprint.route('/', methods=["GET", "POST"])
def index():
    students = Student.query.all()
    result = [student.to_dict() for student in students]
    return jsonify({"status": "success", "data": result}), 200


@student_blueprint.route("/view/<int:user_id>", methods=["GET"])
def view(user_id):
    result = db.session.execute(f"SELECT * FROM student WHERE id=%s" % user_id).one()
    return Response(response=json.dumps({"status": "success", "data": dict(result)}), content_type="application/json")


@student_blueprint.route('/add', methods=["POST"])
def add():
    student = Student(name=request.form.get("name"), age=request.form.get("age"))
    db.session.add(student)
    db.session.commit()
    return jsonify({"status": "success", "data": student.to_dict()})


@student_blueprint.route('/edit/student_<int:user_id>', methods=["PUT", "POST"])
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


@student_blueprint.route('/delete/student_<int:user_id>', methods=["DELETE"])
def delete(user_id):
    query = Student.query.get(user_id)
    db.session.delete(query)
    db.session.commit()
    return jsonify({"staus": "success", "data": ['deleted', query.to_dict()]}), 200
