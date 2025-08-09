import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from app.main import app

client = TestClient(app)


def test_get_flights(monkeypatch):
    async def mock_fetch_flights(origin, destination, date):
        return [
            {
                "flight_number": "AB123",
                "origin": origin,
                "destination": destination,
                "date": date,
                "price": 100.0,
            }
        ]

    monkeypatch.setattr("app.main.fetch_flights", mock_fetch_flights)
    response = client.get(
        "/flights",
        params={"origin": "AAA", "destination": "BBB", "date": "2023-01-01"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body[0]["price"] == 100.0


def test_create_alert(monkeypatch):
    async def mock_monitor_price(origin, destination, date, price, interval=60):
        return None

    monkeypatch.setattr("app.main.monitor_price", mock_monitor_price)
    response = client.post(
        "/alerts",
        json={
            "origin": "AAA",
            "destination": "BBB",
            "date": "2023-01-01",
            "price": 50.0,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Alert created"}
