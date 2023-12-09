from fastapi import Depends, routing
from typing import Annotated

from admin.crud import get_current_user
from admin.schema import UserBase


router = routing.APIRouter()


@router.get("/users/me")
async def read_users_me(current_user: Annotated[UserBase, Depends(get_current_user)]):
    return current_user
