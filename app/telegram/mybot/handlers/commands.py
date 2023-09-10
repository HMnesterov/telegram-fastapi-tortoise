from app.telegram.mybot.deps import dp
from aiogram import types

from app.telegram.mybot.service import save_tg_message


@dp.message_handler()
async def catch_user_message(message: types.Message) -> None:
    await save_tg_message(tg_msg=message, tg_user=message.from_user, tg_chat=message.chat)
