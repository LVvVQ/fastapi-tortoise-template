import pytest
from httpx import AsyncClient

from tests.conftest import USER_EMAIL, USER_NAME, USER_PASSWORD


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    data = {"username": USER_NAME, "email": USER_EMAIL, "password": USER_PASSWORD}
    response = await client.post("/users", json=data)
    assert response.status_code == 201
    assert "password" not in response.json()


@pytest.mark.anyio
async def test_create_user_with_invalid_email(client):
    data = {"name": "Keshari Nandan", "email": "keshari.com", "password": USER_PASSWORD}
    response = await client.post("/users/", json=data)
    assert response.status_code != 201


@pytest.mark.anyio
async def test_create_user_with_empty_password(client):
    data = {"name": "Keshari Nandan", "email": USER_EMAIL, "password": ""}
    response = await client.post("/users/", json=data)
    assert response.status_code != 201


@pytest.mark.anyio
async def test_create_user_with_numeric_password(client):
    data = {"name": "Keshari Nandan", "email": USER_EMAIL, "password": "1232382318763"}
    response = await client.post("/users/", json=data)
    assert response.status_code != 201


@pytest.mark.anyio
async def test_create_user_with_char_password(client):
    data = {"name": "Keshari Nandan", "email": USER_EMAIL, "password": "asjhgahAdF"}
    response = await client.post("/users/", json=data)
    assert response.status_code != 201


@pytest.mark.anyio
async def test_create_user_with_alphanumeric_password(client):
    data = {"name": "Keshari Nandan", "email": USER_EMAIL, "password": "sjdgajhGG27862"}
    response = await client.post("/users/", json=data)
    assert response.status_code != 201
