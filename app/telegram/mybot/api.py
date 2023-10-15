from typing import List

from fastapi.params import Depends
from .deps import *
from .models import *
from .events import *
from app.telegram.mybot.handlers.commands import *
from app.auth.dao import WebUser
from app.auth.service import get_current_active_user


@app.get("/users")
async def get_users_list(limit: int, offset: int, _: WebUser = Depends(get_current_active_user)) -> List[TGUserJson]:
    """Get users with limit and set params"""
    return await TGUserJson.from_queryset(TGUser.all().limit(limit).offset(offset))


@app.get("/users/{user_id}")
async def get_current_user(user_id: int, _: WebUser = Depends(get_current_active_user)) -> TGUserJson:
    """Get current user"""
    return await TGUserJson.from_queryset_single(TGUser.get_or_none(id=user_id))


@app.get("/chats")
async def get_chats_list(limit: int, offset: int, _: WebUser = Depends(get_current_active_user)) -> List[TGChatJson]:
    """Get chats with limit and set params"""
    return await TGChatJson.from_queryset(TGChat.all().limit(limit).offset(offset))


@app.get("/chats/{chat_id}")
async def get_current_chat(chat_id: int, _: WebUser = Depends(get_current_active_user)) -> TGChatJson:
    """Get current chat"""
    return await TGChatJson.from_queryset_single(TGChat.get_or_none(id=chat_id))


@app.get("/messages/{chat_id}")
async def get_messages_by_chat(chat_id: int, limit: int, offset: int, _: WebUser = Depends(get_current_active_user)) -> List[TGMessageJson]:
    """Get messages with limit and offset params by chat"""
    messages = await TGMessage.filter(chat_id=chat_id).select_related("author", "user").limit(limit).offset(offset)
    return [TGMessageJson.from_orm(msg) for msg in messages]


@app.get("/messages/{chat_id}/{message_id}")
async def get_current_message(chat_id: int, message_id: int,
                              _: WebUser = Depends(get_current_active_user)) -> TGMessageJson:
    """Get current message"""
    return await TGMessageJson.from_queryset_single(TGMessage.get_or_none(chat_id=chat_id, id=message_id))
