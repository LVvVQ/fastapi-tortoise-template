import pytest
from httpx import AsyncClient

from tests.conftest import USER_EMAIL, USER_NAME, USER_PASSWORD


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    data = {"username": USER_NAME, "email": USER_EMAIL, "password": USER_PASSWORD}
    response = await client.post("/users", json=data)
    assert response.status_code == 201
    assert "password" not in response.json()
