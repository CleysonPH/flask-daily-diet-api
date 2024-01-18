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


@bp.route("/<int:id>", methods=("GET",))
def get_by_id(id):
    meal = MealRepository.get_by_id(id)
    if meal:
        return meal.to_dict()
    return {"message": "Meal not found"}, 404


@bp.route("/<int:id>", methods=("DELETE",))
def delete(id):
    meal = MealRepository.get_by_id(id)
    if meal:
        MealRepository.delete(meal)
        return {}, 204
    return {"message": "Meal not found"}, 404


@bp.route("/<int:id>", methods=("PUT",))
def update(id):
    meal = MealRepository.get_by_id(id)
    if meal:
        data = request.get_json()
        meal = MealRepository.update(
            meal,
            name=data["name"],
            description=data["description"],
            datetime=datetime.fromisoformat(data["datetime"]),
            in_diet=data["in_diet"],
        )
        return meal.to_dict()
    return {"message": "Meal not found"}, 404
