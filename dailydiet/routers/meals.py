from flask import Blueprint, request

from dailydiet.repositories.meal import MealRepository

bp = Blueprint("meals", __name__, url_prefix="/api/meals")


@bp.route("", methods=("POST",))
def create():
    data = request.get_json()
    meal = MealRepository.create(
        name=data["name"],
        description=data["description"],
        datetime=data["datetime"],
        in_diet=data["in_diet"],
    )
    return meal.to_dict(), 201
