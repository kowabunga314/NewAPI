from fastapi import Depends, routing
from pydantic import BaseModel, EmailStr
from typing import Annotated

from core.security import oauth2_scheme


router = routing.APIRouter()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_decode_token(token):
    return UserOut(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@router.get("/users/me")
async def read_users_me(current_user: Annotated[UserBase, Depends(get_current_user)]):
    return current_user
