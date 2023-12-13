from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from core.crud import CRUDBase
from core.utilities import get_db
from product.models import Product
from product.schema import ProductCreate, ProductUpdate

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProductCreate, owner_id: int
    ) -> Product:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
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
