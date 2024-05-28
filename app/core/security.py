from passlib.context import CryptContext
from typing_extensions import Union
from datetime import datetime, timezone, timedelta
from core.config import settings
from jose import jwt
from pydantic import ValidationError
from fastapi import HTTPException, status
# My dependecies
from schemas.auth_schema import TokenPayload


password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(tz=timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp" : expires_delta,
        "sub" : str(subject)
    }
    
    jwt_encode = jwt.encode(
        info_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encode

def create_refresh_token(subject: Union[str, any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(tz=timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }
    
    jwt_encode = jwt.encode(
        info_jwt,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encode

def refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_REFRESH_SECRET_KEY,
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
    
    return create_access_token(token_data.sub)