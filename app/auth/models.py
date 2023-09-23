from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .dao import WebUser

WebUserJSON = pydantic_model_creator(WebUser, exclude=('hashed_password',))

class TokenData(BaseModel):
    access_token: str | None
    token_type: str | None
    username: str