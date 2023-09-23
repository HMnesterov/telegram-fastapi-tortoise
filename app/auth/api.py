from fastapi import Depends, HTTPException
from starlette import status
from .dao import WebUser
from .deps import app
from .models import WebUserJSON, TokenData
from .service import *
from fastapi.security import OAuth2PasswordRequestForm


@app.post('/register', response_model=TokenData)
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    """Создаётся новый пользователь, выдаётся временный токен"""
    if await WebUser.exists(username=form_data.username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User with this name already exists!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    hashed_password = get_password_hash(form_data.password)
    user = await WebUser.create(username=form_data.username, hashed_password=hashed_password, disabled=False)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return TokenData(access_token=access_token, token_type="bearer", username=form_data.username)

@app.post("/token", response_model=TokenData)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return TokenData(access_token=access_token, token_type="bearer", username=form_data.username)

@app.get("/users/me/", response_model=WebUserJSON)
async def read_users_me(current_user: WebUser = Depends(get_current_active_user)):
    return current_user
