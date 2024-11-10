from pydantic import BaseModel


class RegisterUserRequest(BaseModel):
    username: str
    email: str
    password: str
