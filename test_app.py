from app import app

def test_sanity():
    assert 1 + 1 == 2

def test_get_tasks():
    client = app.test_client()
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_post_task():
    client = app.test_client()
    response = client.post("/api/tasks", json={"text": "test task", "quadrant": "q1", "completed": False})
    assert response.status_code == 200
    task_id = response.json["id"]
    tasks = client.get("/api/tasks").json
    assert any(t["id"] == task_id for t in tasks)
    client.delete(f"/api/tasks/{task_id}")