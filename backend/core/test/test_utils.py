from datetime import timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from admin.crud import user as crud_user
from core.settings import settings
from core.security import create_access_token
from core.utilities import get_db


username = 'a@b.c'
password = 'password'


def authenticate(
        db: Session = Depends(get_db),
        email: str = username,
        password: str = password
):
    user = crud_user.authenticate(
        db=db, email=email, password=password
    )
    if not user:
        raise ValueError("Incorrect email or password")
    elif not crud_user.is_active(user):
        raise ValueError("Inactive user")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
