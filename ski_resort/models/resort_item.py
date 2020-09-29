from datetime import datetime
from db import db


class ResortItem(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    updated = db.Time(db.TIME())

    def __init__(self, name: str):
        self.name = name
        self.updated = datetime.today()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> 'ResortItem':
        return cls.query.filter_by(username=name).first()

    @classmethod
    def find_by_id(cls, _id: int) -> 'ResortItem':
        return cls.query.filter_by(id=_id).first()
