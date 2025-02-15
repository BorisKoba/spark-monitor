from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_submit_log():
    response = client.post("/submit_log/", json={
        "job_id": "job_123",
        "run_length": 300,
        "executor_count": 5,
        "operators": ["Read CSV", "Filter", "Sort"],
        "operator_lengths": [50, 100, 150]
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Log saved successfully"}