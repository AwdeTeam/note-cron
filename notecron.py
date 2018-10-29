# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Runnable for the flask app."""

from app import app, db


@app.shell_context_processor
def make_shell_context():
    return {'db': db}
