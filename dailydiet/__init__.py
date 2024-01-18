from flask import Flask


def create_app():
    app = Flask(__name__)

    from dailydiet.ext import database

    database.init_app(app)

    from dailydiet.routers import ping

    app.register_blueprint(ping.bp)

    return app
