import os

import pytest

from dailydiet import create_app


@pytest.fixture()
def app():
    os.environ["APP_SETTINGS"] = "dailydiet.config.TestConfig"
    app = create_app()
    with app.app_context():
        from dailydiet.ext.database import db

        db.create_all()

        yield app

        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
