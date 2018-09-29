from app import db


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64), index=True, unique=True)
    server = db.Column(db.String(64))
    armory_link = db.Column(db.String(128))
    ilvl = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Character {}>'.format(self.name)
