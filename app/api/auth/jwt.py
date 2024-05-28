from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
# My dependencies
from schemas.auth_schema import TokenSchema
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token, refresh_token
from models.user_model import User
from api.dependencies.user_deps import get_current_user


auth_router = APIRouter()

@auth_router.post('/login',
                  summary='Cria Access Token e Refresh Token',
                  response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.authenticate(
        email = data.username,
        password = data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou senha incorretos'
        )
    
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }

@auth_router.post('/test')
async def test(data: User = Depends(get_current_user)):
    return data

@auth_router.post('/new_token',
                  summary='Atuailiza o Access Token',
                  response_model=TokenSchema)
async def new_token(data: str):
    print(data)
    return {
        "access_token": refresh_token(data),
        "refresh_token": data
    }