import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_list_flights():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/flights/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_create_and_get_flight():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp_post = await ac.post("/flights/", json={"id": 99, "origin": "SFO", "destination": "LAS"})
        assert resp_post.status_code == 201
        resp_get = await ac.get("/flights/99")
        assert resp_get.status_code == 200
        assert resp_get.json()["origin"] == "SFO"
