from fastapi import APIRouter, status

from app.responses.user import UserResponse
from app.schemas.user import RegisterUserRequest
from app.services import user

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@user_router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(data: RegisterUserRequest):
    return await user.create_user_account(data)
