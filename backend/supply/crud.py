from fastapi.encoders import jsonable_encoder
import logging
from sqlalchemy.orm import Session
from typing import List

from core.crud import CRUDBase
from supply.models import MaterialCost, ProductionCost
from supply.schema import (
    MaterialCostCreate, MaterialCostUpdate,
    ProductionCostCreate, ProductionCostUpdate
)


logger = logging.getLogger('abacus.supply.crud')


class CRUDMaterialCost(CRUDBase[MaterialCost, MaterialCostCreate, MaterialCostUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: MaterialCostCreate, owner_id: int
    ) -> MaterialCost:
        logger.debug('CRUD creating object.')
        obj_in_data = jsonable_encoder(obj_in)
        logger.debug('JSON-encoded input object.')
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        logger.debug('Converted input object to model.')
        db.add(db_obj)
        logger.debug('Added input object to DB.')
        db.commit()
        logger.debug('Committed change to DB.')
        db.refresh(db_obj)
        logger.debug('Refreshed model from DB.')
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[MaterialCost]:
        return (
            db.query(self.model)
            .filter(MaterialCost.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

material_cost = CRUDMaterialCost(MaterialCost)


class CRUDProductionCost(CRUDBase[ProductionCost, ProductionCostCreate, ProductionCostUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProductionCostCreate, owner_id: int
    ) -> ProductionCost:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[ProductionCost]:
        return (
            db.query(self.model)
            .filter(ProductionCost.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

production_cost = CRUDProductionCost(ProductionCost)
