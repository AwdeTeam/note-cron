# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Database table models."""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(UserMixin, db.Model):
    """Model class representing a user."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """Create the password hash from parameter."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Run the hash of the parameter versus the user's stored password hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {0}:{1}>".format(self.id, self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
