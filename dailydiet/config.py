import os


class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", False)
    SECRET_KEY = os.environ.get("SECRET_KEY", None)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", None)


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
