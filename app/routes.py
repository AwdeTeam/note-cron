# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""For now, just the home page route."""

from app import app

@app.route('/')
@app.route('/index')
def index():
    """Simple hello world test."""
    return "Hello world"
