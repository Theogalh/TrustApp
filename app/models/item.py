from app import db
from app.models.character import char_item


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.relationship("Character",
                                 secondary=char_item,
                                 back_populates='items',
                                 lazy='dynamic')
    name = db.Column(db.String(64), index=True, unique=True)
    ilvl = db.Column(db.Integer, index=True)
    emplacement = db.Column(db.String(64), index=True)


    def __repr__(self):
        return '<Item {}>'.format(self.name)
