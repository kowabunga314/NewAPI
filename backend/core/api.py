from fastapi import APIRouter

from admin.endpoints import router as admin_router
# from core.security import router as security_router
from product.endpoints import router as product_router
from supply.endpoints import router as supply_router

router = APIRouter()
router.include_router(admin_router, prefix='/admin', tags=['admin'])
router.include_router(product_router, prefix='/product', tags=['product'])
# router.include_router(security_router, prefix='/auth', tags=['security'])
router.include_router(supply_router, prefix='/supply', tags=['supply'])
