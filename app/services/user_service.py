from schemas.user_schema import UserAuth, NewUser
from models.user_model import User
from typing_extensions import Optional
from core.security import verify_password, get_password
from uuid import UUID


class UserService:
    @staticmethod
    async def create_user(user: NewUser):
        user = User(
            email = user.email,
            hash_password = get_password(user.password),
            birthdate = user.birthdate,
            gender = user.gender,
            first_name = user.first_name,
            last_name = user.last_name,
        )
        
        await user.save()
        return user
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(
            password=password,
            hashed_password=user.hash_password
        ):
            return None
        
        return user
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def get_user_by_uuid(id: UUID) -> User:
        user = await User.find_one(User.user_id == id)
        return user