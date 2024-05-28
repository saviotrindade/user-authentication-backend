from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import date
from custom_types.user_types import Gender


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="E-mail do Usuário")
    # birthdate: date = Field(
    #     ...,
    #     description='Data de nascimento'
    # )
    password: str = Field(
        ...,
        min_length=5,
        max_length=20,
        description='Senha do Usuário'
    )

class NewUser(UserAuth):
    birthdate: date = Field(..., description="Data de nascimento.")
    first_name: str = Field(..., description="Primeiro nome.")
    last_name: str = Field(..., description="Sobrenome.")
    gender: Gender = Field(..., description="Genero")

class UserDetail(BaseModel):
    user_id: UUID
    email: str
    first_name: str
    last_name: str
    
