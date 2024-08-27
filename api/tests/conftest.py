from typing import AsyncGenerator

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from api.api import api


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncGenerator:
    async with (
        AsyncClient(
            transport=ASGITransport(app=api),  # type: ignore
            base_url="http://testserver:8001",
        ) as client,
        LifespanManager(api),
    ):
        yield client
