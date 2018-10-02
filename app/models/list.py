from app import db
from datetime import datetime

list_char = db.Table('list_char',
                     db.Column('list_id', db.Integer, db.ForeignKey('list.id')),
                     db.Column('char_id', db.Integer, db.ForeignKey('character.id'))
                     )


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(64), index=True, unique=True)
    last_update = db.Column(db.DateTime, default=datetime.now)
    characters = db.relationship('Character', secondary=list_char,
                                 back_populates='lists',
                                 lazy='dynamic')

    def __repr__(self):
        return '<List {}>'.format(self.name)

    def refresh(self):
        self.last_update = datetime.now()
        for char in self.characters:
            char.refresh()
