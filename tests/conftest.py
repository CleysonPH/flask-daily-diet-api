import os
from datetime import datetime

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


@pytest.fixture()
def meals(app):
    with app.app_context():
        from dailydiet.ext.database import db
        from dailydiet.models import Meal

        meals = [
            Meal(
                name="Breakfast",
                description="A delicious breakfast",
                datetime=datetime.fromisoformat("2019-01-01T08:00:00.000"),
                in_diet=False,
            ),
            Meal(
                name="Lunch",
                description="A delicious lunch",
                datetime=datetime.fromisoformat("2019-01-01T12:00:00.000"),
                in_diet=False,
            ),
            Meal(
                name="Dinner",
                description="A delicious dinner",
                datetime=datetime.fromisoformat("2019-01-01T19:00:00.000"),
                in_diet=False,
            ),
        ]

        db.session.bulk_save_objects(meals)
        db.session.commit()
        return Meal.query.all()
