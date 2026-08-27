def test_get_activities_returns_seed_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Science Club" in data


def test_get_activities_item_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()

    for details in activities.values():
        assert set(details.keys()) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(details["description"], str)
        assert isinstance(details["schedule"], str)
        assert isinstance(details["max_participants"], int)
        assert isinstance(details["participants"], list)
