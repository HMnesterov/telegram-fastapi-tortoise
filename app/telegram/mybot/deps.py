from aiogram import Bot, Dispatcher, types
from fastapi import APIRouter
from core.settings import settings

app = APIRouter()

bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)


@app.on_event("startup")
async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=settings.WEBHOOK_URL + '/api/webhook')


@app.post(f'/webhook')
async def bot_webhook(update: dict) -> None:
    """In this method, we receive user's messages from webhook post requests"""
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(update=types.Update(**update))
