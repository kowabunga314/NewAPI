from fastapi import APIRouter
import logging

from admin.endpoints.login import router as login_router
from admin.endpoints.user import router as user_router
# from core.security import router as security_router
from product.endpoints import router as product_router
# from supply.endpoints import router as supply_router


# create logger
logger = logging.getLogger('abacus')
logger.setLevel(logging.DEBUG)
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# # add formatter to ch
# ch.setFormatter(formatter)
# # add ch to logger
# if (logger.hasHandlers()):
#     logger.handlers.clear()
# logger.addHandler(ch)

router = APIRouter()
router.include_router(login_router, prefix='/login', tags=['admin', 'login'])
router.include_router(product_router, tags=['product'])
# router.include_router(security_router, prefix='/auth', tags=['security'])
# router.include_router(supply_router, prefix='/supply', tags=['supply'])
router.include_router(user_router, prefix='/user', tags=['admin', 'user'])
