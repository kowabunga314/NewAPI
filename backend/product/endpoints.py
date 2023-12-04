from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from core.utilities import get_db
from product.schema import Product


router = APIRouter()


@router.get("/{product_id}/", response_model=Product)
async def read_product(*, db: Session = Depends(get_db), product_id) -> Any:
    return None

@router.get("/", response_model=list[Product])
async def query_product(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.put("/", response_model=Product)
async def create_product(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.post("/", response_model=Product)
async def update_product(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.delete("/{product_id}")
async def delete_product(*, db: Session = Depends(get_db), product_id) -> Any:
    return None
