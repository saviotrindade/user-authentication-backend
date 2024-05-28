from pydantic import Field, EmailStr
from uuid import UUID, uuid4
# Beanie
from beanie import Document, Indexed
# Standard Collections
from datetime import date, datetime
from typing_extensions import Annotated
# My dependencies
from custom_types.user_types import Gender

    
class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    email: Annotated[EmailStr, Indexed(unique=True)]
    birthdate: date
    gender: Gender
    hash_password: str
    first_name: str
    last_name: str
    disabled: bool = False
    
    def __repr__(self) -> str:
        return f'User {self.email}'
    
    def __str__(self) -> str:
        return self.email
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False
    
    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(self, email:str) -> "User":
        return await self.find_one(self.email == email)