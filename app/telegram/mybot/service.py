from aiogram import types
from app.telegram.mybot.dao import TGUser, TGChat, TGMessage
from hashlib import md5


async def __get_updated_user(tg_user: types.User) -> TGUser:
    user: TGUser = await TGUser.get_or_none(id=tg_user.id)
    user_hash = md5(fr"{tg_user.first_name}-{tg_user.username}-{tg_user.language_code}".encode("utf-8")).hexdigest()
    if user is None:
        user = await TGUser.create(hash=user_hash, **tg_user.to_python())
    elif user.hash != user_hash:
        await user.update_from_dict(tg_user.to_python())
        await user.save()
    return user


async def __get_updated_chat(tg_chat: types.Chat) -> TGChat:
    chat: TGChat = await TGChat.get_or_none(id=tg_chat.id)
    chat_hash = md5(fr"{tg_chat.first_name}-{tg_chat.type}".encode("utf-8")).hexdigest()
    if chat is None:
        chat = await TGChat.create(hash=chat_hash, **tg_chat.to_python())
    elif chat.hash != chat_hash:
        await chat.update_from_dict(tg_chat.to_python())
        await chat.save()
    return chat


async def save_tg_message(tg_msg: types.Message, tg_user: types.User, tg_chat: types.Chat) -> TGMessage:
    # step 1 - get/update user
    user: TGUser = await __get_updated_user(tg_user)

    # step 2 - get/update chat
    chat: TGChat = await __get_updated_chat(tg_chat)

    # step 3 - create message
    return await TGMessage.create(chat=chat,
                                  author=user,
                                  id=tg_msg.message_id,
                                  text=tg_msg.text,
                                  created_at=tg_msg.date)
