from fastapi.encoders import jsonable_encoder
import logging
from sqlalchemy.orm import Session
from typing import List

from core.crud import CRUDBase
from core.utilities import get_db
from product.models import Product
from product.schema import ProductCreate, ProductUpdate
from supply.models import MaterialCost


logger = logging.getLogger('abacus.product.curl')

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProductCreate, owner_id: int
    ) -> Product:
        logger.info('Creating model with owner.')
        obj_in_data = jsonable_encoder(obj_in)
        logger.info(f'Input data: {obj_in_data}')
        db_obj = self.model(
            **obj_in_data,
            owner_id=owner_id,
            # material_cost_ids=db.query(MaterialCost).filter(MaterialCost.id.in_(material_cost_ids)).all() if len(material_costs) > 0 else []
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        return (
            db.query(self.model)
            .filter(Product.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


product = CRUDProduct(Product)
