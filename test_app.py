from app import app

def test_sanity():
    assert 1 + 1 == 2

def test_get_tasks():
    client = app.test_client()
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)