import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ["APP_SETTINGS"])

    from dailydiet import models  # noqa: F401
    from dailydiet.ext import database, migrate

    database.init_app(app)
    migrate.init_app(app)

    from dailydiet.routers import ping

    app.register_blueprint(ping.bp)

    return app
