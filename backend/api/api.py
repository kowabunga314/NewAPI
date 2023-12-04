from fastapi import APIRouter

from product.endpoints import router as product_router
from supply.endpoints import router as supply_router

router = APIRouter()
router.include_router(product_router, prefix='/product', tags=['product'])
router.include_router(supply_router, prefix='/supply', tags=['supply'])
