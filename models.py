from datetime import datetime
from sqlalchemy import true
from config import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session
        load_instance = true
