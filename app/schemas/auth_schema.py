from pydantic_settings import BaseSettings
from uuid import UUID


class TokenSchema(BaseSettings):
    access_token: str
    refresh_token: str

class TokenPayload(BaseSettings):
    sub: UUID = None
    exp: int = None