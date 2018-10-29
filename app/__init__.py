# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Flask application instance."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
