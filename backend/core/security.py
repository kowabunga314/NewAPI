from fastapi import Depends, routing
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated


router = routing.APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
