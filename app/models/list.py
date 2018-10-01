from app import db
from datetime import datetime


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(64), index=True, unique=True)
    last_update = db.Column(db.DateTime, default=datetime.now)

    def refresh(self):
        self.last_update = datetime.now()
        # TODO Parcourir les characters, et les mettre a jour.
        db.session.commit()
