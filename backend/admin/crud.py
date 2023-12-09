from fastapi import Depends, routing
from typing import Annotated

from admin.schema import UserOut
from core.security import oauth2_scheme


router = routing.APIRouter()


def fake_decode_token(token):
    return UserOut(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user
