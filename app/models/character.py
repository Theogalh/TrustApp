from app import db
import datetime


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO A voir a faire une relation ManyToMany
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))
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
