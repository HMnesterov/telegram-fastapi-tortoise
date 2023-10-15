import pytest
from core.app import app
from tortoise import Tortoise
from httpx import AsyncClient
from core.migrate import migrate
from asgi_lifespan import LifespanManager


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module")
async def client():
    await Tortoise.init(
        db_url='sqlite://:memory:',
        modules={
            "migrate": ["core.migrate"],
            "models": ["app.telegram.mybot.dao"]

        }
    )
    await migrate()
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
    await Tortoise.close_connections()