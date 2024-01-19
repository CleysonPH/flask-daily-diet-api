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


def test_create_meal_invalid_data(client):
    request_body = {
        "description": "A",
        "datetime": "2019-01-01T08:00:00.000 ss",
        "in_diet": False,
    }
    response = client.post("/api/meals", json=request_body)
    assert response.status_code == 400
    assert "name" in response.json["errors"]
    assert "description" in response.json["errors"]
    assert "datetime" in response.json["errors"]


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


def test_delete_meal(client, meals):
    meal = meals[0]
    response = client.delete(f"/api/meals/{meal.id}")
    assert response.status_code == 204
    assert response.data == b""
    response = client.get(f"/api/meals/{meal.id}")
    assert response.status_code == 404
    assert response.json["message"] == "Meal not found"


def test_delete_meal_not_found(client):
    response = client.delete("/api/meals/1")
    assert response.status_code == 404
    assert response.json["message"] == "Meal not found"


def test_update_meal(client, meals):
    meal = meals[0]
    request_body = {
        "name": "Breakfast Edited",
        "description": "A delicious breakfast Edited",
        "datetime": "2019-01-01T08:00:00.000",
        "in_diet": True,
    }
    response = client.put(f"/api/meals/{meal.id}", json=request_body)
    assert response.status_code == 200
    assert response.json["id"] == meal.id
    assert response.json["name"] == request_body["name"]
    assert response.json["description"] == request_body["description"]


def test_update_meal_not_found(client):
    request_body = {
        "name": "Breakfast Edited",
        "description": "A delicious breakfast Edited",
        "datetime": "2019-01-01T08:00:00.000",
        "in_diet": True,
    }
    response = client.put("/api/meals/1", json=request_body)
    assert response.status_code == 404
    assert response.json["message"] == "Meal not found"
