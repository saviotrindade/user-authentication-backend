from decouple import config
from pydantic import AnyHttpUrl 
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str)
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1",
    ]
    PROJECT_NAME: str = "Auth"
    
    # Database
    MONGO_CONNECTION_STRING: str = config('MONGO_CONNECTION_STRING', cast=str)
    
    class Config:
        case_sensitive = True

settings = Settings()