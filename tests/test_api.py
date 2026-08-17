from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_existing_client():
    response = client.get("/clients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Aarav Mehta"


def test_get_unknown_client_returns_404():
    response = client.get("/clients/999")
    assert response.status_code == 404


def test_create_client():
    payload = {"name": "Neha Kapoor", "risk_level": "Low", "balance": 50000}
    response = client.post("/clients", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Neha Kapoor"


def test_create_client_rejects_negative_balance():
    payload = {"name": "Invalid Client", "risk_level": "Low", "balance": -100}
    response = client.post("/clients", json=payload)
    assert response.status_code == 422
