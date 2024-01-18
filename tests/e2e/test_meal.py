def test_create_meal(client):
    request_body = {
        "name": "Breakfast",
        "description": "A delicious breakfast",
        "datetime": "2019-01-01T08:00:00.000",
        "in_diet": False,
    }
    response = client.post("/api/meals", json=request_body)
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["name"] == request_body["name"]
    assert response.json["description"] == request_body["description"]


def test_get_all_meals(client, meals):
    response = client.get("/api/meals")
    assert response.status_code == 200
    assert len(response.json["meals"]) == len(meals)
    for meal in meals:
        assert any(
            m["id"] == meal.id
            and m["name"] == meal.name
            and m["description"] == meal.description
            for m in response.json["meals"]
        )


def test_get_meal_by_id(client, meals):
    meal = meals[0]
    response = client.get(f"/api/meals/{meal.id}")
    assert response.status_code == 200
    assert response.json["id"] == meal.id
    assert response.json["name"] == meal.name
    assert response.json["description"] == meal.description


def test_get_meal_by_id_not_found(client):
    response = client.get("/api/meals/1")
    assert response.status_code == 404
    assert response.json["message"] == "Meal not found"
