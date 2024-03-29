from dailydiet.ext.database import db
from dailydiet.models import Meal


class MealRepository:
    @staticmethod
    def create(name, description, datetime, in_diet):
        meal = Meal(
            name=name,
            description=description,
            datetime=datetime,
            in_diet=in_diet,
        )
        db.session.add(meal)
        db.session.commit()
        return meal

    @staticmethod
    def get_all():
        return db.session.query(Meal).all()

    @staticmethod
    def get_by_id(id):
        return db.session.get(Meal, id)

    @staticmethod
    def delete(meal):
        db.session.delete(meal)
        db.session.commit()

    @staticmethod
    def update(meal, name, description, datetime, in_diet):
        meal.name = name
        meal.description = description
        meal.datetime = datetime
        meal.in_diet = in_diet
        db.session.commit()
        return meal
