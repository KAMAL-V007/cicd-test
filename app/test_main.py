import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app

@pytest.fixture
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_create_and_list_task(client):
    # Create
    response = await client.post("/tasks/", json={"title": "Test CI", "completed": False})
    assert response.status_code == 200, f"Response: {response.text}"
    data = response.json()
    assert data["title"] == "Test CI"
    
    # List
    response = await client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) > 0