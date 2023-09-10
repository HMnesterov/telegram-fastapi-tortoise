from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from datetime import datetime
from .dao import *

# TGUser for api
TGUserJson = pydantic_model_creator(TGUser, exclude=("hash",))

# TGChat for api
TGChatJson = pydantic_model_creator(TGChat, exclude=("hash",))


# TGMessage for api
class TGMessageJson(PydanticModel):
    id: int
    author: TGUserJson
    chat: TGChatJson
    text: str
    created_at: datetime
