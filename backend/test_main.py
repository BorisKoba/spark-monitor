import os
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

def test_submit_log_missing_field():
    response = client.post("/submit_log/", json={
        "job_id": "job_124",
        "run_length": 200,
        "executor_count": 4,
        "operators": ["Read CSV", "Filter"]
    })
    assert response.status_code == 422

def test_submit_log_invalid_data():
    response = client.post("/submit_log/", json={
        "job_id": "job_125",
        "run_length": "invalid_data",
        "executor_count": 3,
        "operators": ["Read CSV"],
        "operator_lengths": [50]
    })
    assert response.status_code == 422

def test_get_logs():
    response = client.get("/logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_submit_log_file_created():
    job_data = {
        "job_id": "job_126",
        "run_length": 150,
        "executor_count": 2,
        "operators": ["Read CSV"],
        "operator_lengths": [50]
    }
    client.post("/submit_log/", json=job_data)
    log_file = f"./iceberg_logs/{job_data['job_id']}.json"
    assert os.path.exists(log_file)
