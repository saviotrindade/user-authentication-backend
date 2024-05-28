from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import NewUser
from services.user_service import UserService
from email_validator import validate_email, EmailNotValidError
import pymongo
from pydantic_settings import BaseSettings


class ValidateUsername(BaseSettings):
    username: str

user_router = APIRouter()

@user_router.post('/add')
async def add_user(data : NewUser):
    try:
        return await UserService.create_user(data)
    except pymongo.error.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )

@user_router.post('/email_validation')
async def validation(data: ValidateUsername):
    try:
        validate_email(data.username, check_deliverability = True)
        return True
    except EmailNotValidError:
        return False
        

@user_router.get('/email_exists')
async def check_email(username : str) -> bool:
    user = await UserService.get_user_by_email(username)
    if user is not None:
        return True
    return False