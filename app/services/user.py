from fastapi import BackgroundTasks, HTTPException

from app.config.security import hash_password
from app.models.user import User
from app.schemas.user import RegisterUserRequest
from app.services.email import send_account_verification_email


async def create_user_account(
    data: RegisterUserRequest, background_tasks: BackgroundTasks
):
    user_is_exist = await User.exists(email=data.email)
    if user_is_exist:
        raise HTTPException(status_code=400, detail="Email already exists.")

    data.password = hash_password(data.password)
    user = await User.create(**data.model_dump(exclude_unset=True))

    await send_account_verification_email(user, background_tasks=background_tasks)

    return user
