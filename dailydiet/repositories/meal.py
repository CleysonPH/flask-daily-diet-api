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
        return Meal.query.all()

    @staticmethod
    def get_by_id(id):
        return Meal.query.get(id)
