from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "age": self.age}
        else:
            return {"col": getattr(self, col) for col in columns}