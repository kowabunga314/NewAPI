from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from admin import crud as user_crud
from admin import models as user_model
from admin import schema as user_schema
from core.settings import settings
from core.utilities import get_db, get_current_active_user, get_current_active_superuser
from app_email.app_email import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[user_schema.User])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: user_model.User = Depends(get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = user_crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=user_schema.User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: user_schema.UserCreate,
    current_user: user_model.User = Depends(get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = user_crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user_crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
        print('send email')
    return user


@router.put("/me", response_model=user_schema.User)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: user_model.User = Depends(get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = user_schema.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = user_crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=user_schema.User)
def read_user_me(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=user_schema.User)
def create_user_open(
    *,
    db: Session = Depends(get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = user_crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = user_schema.UserCreate(password=password, email=email, full_name=full_name)
    user = user_crud.user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=user_schema.User)
def read_user_by_id(
    user_id: int,
    current_user: user_model.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not user_crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=user_schema.User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: user_schema.UserUpdate,
    current_user: user_model.User = Depends(get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = user_crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = user_crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
