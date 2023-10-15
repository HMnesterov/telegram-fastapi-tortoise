from .migrate import migrate
from tortoise import Tortoise
from core.app import app
from .settings import settings


@app.on_event("startup")
async def on_startup():
    await Tortoise.init(
        db_url=settings.DB_CONNECTION,
        modules={

            "migrate": ["core.migrate"],
            "models": ["app.telegram.mybot.dao",
                       "app.auth.dao"]
        }
    )
    await migrate()


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()