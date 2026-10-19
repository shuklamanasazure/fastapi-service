from fastapi.testclient import TestClient  # Import the FastAPI test client
from app.main import app  # Import the application under test

client = TestClient(app)  # Create an in-process test client

def test_health():  # Verify the health endpoint
    response = client.get("/api/v1/healthz")  # Send a test request
    assert response.status_code == 200  # Require a successful HTTP response
    assert response.json() == {"status": "ok"}  # Validate the response body

def test_info():  # Verify the information endpoint
    response = client.get("/api/v1/info")  # Request application metadata
    assert response.status_code == 200  # Require a successful response
    assert response.json()["name"] == "fastapi-service"  # Verify application identity