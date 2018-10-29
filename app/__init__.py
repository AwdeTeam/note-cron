# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Flask application instance."""

from flask import Flask

app = Flask(__name__)
from app import routes
