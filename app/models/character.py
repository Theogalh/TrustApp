from app import db
from app.models.list import list_char
import datetime


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO A voir a faire une relation ManyToMany
    lists = db.relationship("List",
                            secondary=list_char,
                            back_populates='characters',
                            lazy='dynamic')

    name = db.Column(db.String(64), index=True, unique=True)
    server = db.Column(db.String(64))
    armory_link = db.Column(db.String(128))
    ilvl = db.Column(db.Integer, index=True)
    last_update = datetime.datetime.now()

    def __repr__(self):
        return '<Character {}>'.format(self.name)

    def refresh(self):
        self.last_update = datetime.datetime.now()
        db.session.commit()


char_item = db.Table('char_item',
                     db.Column('char_id', db.Integer, db.ForeignKey('character.id')),
                     db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
                     )
