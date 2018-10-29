# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Database table models."""

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
            

    def __repr__(self):
        return '<User {0}:{1}>'.format(self.id, self.username)
