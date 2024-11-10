from datetime import datetime
from typing import Union

from pydantic import EmailStr

from app.responses.base import BaseRespone


class UserResponse(BaseRespone):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: Union[str, None, datetime] = None
