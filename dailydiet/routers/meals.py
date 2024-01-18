from datetime import datetime

from flask import Blueprint, request

from dailydiet.repositories.meal import MealRepository

bp = Blueprint("meals", __name__, url_prefix="/api/meals")


@bp.route("", methods=("POST",))
def create():
    data = request.get_json()
    meal = MealRepository.create(
        name=data["name"],
        description=data["description"],
        datetime=datetime.fromisoformat(data["datetime"]),
        in_diet=data["in_diet"],
    )
    return meal.to_dict(), 201


@bp.route("", methods=("GET",))
def get_all():
    meals = MealRepository.get_all()
    return {"meals": [meal.to_dict() for meal in meals]}
