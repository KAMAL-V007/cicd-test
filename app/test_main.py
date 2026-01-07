import pytest
from httpx import AsyncClient
from app.main import app
import os

# These tests expect a running Postgres instance
# The GitHub Action must provide this service!

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_create_and_list_task():
    # Verify DB connection is mocked or real
    # In CI, this will connect to the Service Container
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create
        response = await ac.post("/tasks/", json={"title": "Test CI", "completed": False})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test CI"
        
        # List
        response = await ac.get("/tasks/")
        assert response.status_code == 200
        assert len(response.json()) > 0
