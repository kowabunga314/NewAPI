from fastapi import APIRouter
from typing import Any

from product.schema import Product


router = APIRouter()


@router.get("/{product_id}/", response_model=Product)
async def read_product(product_id) -> Any:
    return None

@router.get("/", response_model=list[Product])
async def query_product() -> Any:
    return None

@router.put("/", response_model=Product)
async def create_product() -> Any:
    return None

@router.post("/", response_model=Product)
async def update_product() -> Any:
    return None

@router.delete("/{product_id}")
async def delete_product(product_id) -> Any:
    return None
