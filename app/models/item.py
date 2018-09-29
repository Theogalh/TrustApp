from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    name = db.Column(db.String(64), index=True, unique=True)
    ilvl = db.Column(db.Integer, index=True)
    emplacement = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Character {}>'.format(self.name)
