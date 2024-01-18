import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", False)
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
