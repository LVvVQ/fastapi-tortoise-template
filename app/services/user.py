from fastapi import HTTPException

from app.models.user import User
from app.schemas.user import RegisterUserRequest


async def create_user_account(data: RegisterUserRequest):
    user_is_exist = await User.exists(email=data.email)
    if user_is_exist:
        raise HTTPException(status_code=400, detail="Email already exists.")

    user = await User.create(**data.model_dump(exclude_unset=True))
    return user
