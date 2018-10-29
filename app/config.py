# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Configuration settings for Flask."""

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Class containing all configuration options for Flask."""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASEDIR, "app.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
