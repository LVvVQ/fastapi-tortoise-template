import os
import sys
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

USER_NAME = "test"
USER_EMAIL = "test@gmail.com"
USER_PASSWORD = "password"

ClientManagerType = AsyncGenerator[AsyncClient, None]


@pytest.fixture(scope="function")
def anyio_backend() -> str:
    return "asyncio"


@asynccontextmanager
async def client_manager(app, base_url="http://test", **kw) -> ClientManagerType:
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url=base_url, **kw) as c:
            yield c


@pytest.fixture(scope="function")
async def client() -> ClientManagerType:
    async with client_manager(app) as c:
        yield c
