# Class 16 - RESP API part 2
from flask import Flask
from class_16.models import db
from class_16.controller import student_blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"
app.register_blueprint(student_blueprint, url_prefix="/students")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True, port=16000)
