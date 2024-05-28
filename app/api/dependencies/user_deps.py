from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timezone
from pydantic import ValidationError
# My dependencies
from core.config import settings
from models.user_model import User
from schemas.auth_schema import TokenPayload
from services.user_service import UserService


oauth_reusavel = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT'
)

async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        print(payload)
        token_data = TokenPayload(**payload)
        print(token_data)
        if datetime.fromtimestamp(token_data.exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token expirado.',
                heares={'WWW-Authenticate': 'Bearer'}
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Erro na validação do token',
            headers={'WWW-Authenticate': 'Bearer'}
        )
        
    user = await UserService.get_user_by_uuid(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Usuario não encontrado.',
            headers={'WWW-Authenticate': 'Bearer'}
        )
        
    return user