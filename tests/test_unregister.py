def test_unregister_removes_participant(client):
    email = "daniel@mergington.edu"

    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_when_not_enrolled(client):
    response = client.delete(
        "/activities/Soccer Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_signup_then_unregister_flow(client):
    email = "flow.student@mergington.edu"

    signup_response = client.post(
        "/activities/Art Club/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Art Club/participants",
        params={"email": email},
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    participants = activities_response.json()["Art Club"]["participants"]
    assert email not in participants
