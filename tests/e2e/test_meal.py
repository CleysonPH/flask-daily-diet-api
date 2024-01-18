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
