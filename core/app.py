from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.telegram.mybot.api import app as telegram_app
from app.auth.api import app as auth_app
app = FastAPI()

#include routers
app.include_router(telegram_app, prefix="/api")

app.include_router(auth_app)

#add protection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)