from fastapi.encoders import jsonable_encoder
import json
import logging
from sqlalchemy.orm import Session
from typing import List

from core.crud import CRUDBase
from core.utilities import get_db
from product.models import Product, MaterialCost, ProductionCost
from product.schema import ProductCreate, ProductUpdate, MaterialCostCreate, MaterialCostUpdate, ProductionCostCreate, ProductionCostUpdate


logger = logging.getLogger('abacus.product.curl')

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ProductCreate, owner_id: int
    ) -> Product:
        # Encode input product without material costs
        obj_in_data = jsonable_encoder(obj_in)

        # Get material costs from product
        material_costs = obj_in_data.pop('material_costs')
        logger.info(f'Material cost data: {material_costs}')

        # Create product model
        db_obj = self.model(
            **obj_in_data,
            owner_id=owner_id,
        )

        # Save product to database
        db.add(db_obj)
        # db.commit()
        # db.refresh(db_obj)

        # Query material costs
        # material_costs_db = db.query(MaterialCost).filter(MaterialCost.id.in_(obj_in.material_costs)).all() if len(obj_in.material_costs) > 0 else []
        for mc in material_costs:
            material_cost = db.query(MaterialCost).filter(MaterialCost.id == mc['id']).first()
            if not material_cost:
                raise LookupError(f'Material Cost not found: ID {mc["id"]}')
            db_obj.material_costs.append(material_cost)

        # Commit changes and refresh
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



class CRUDMaterialCost(CRUDBase[MaterialCost, MaterialCostCreate, MaterialCostUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: MaterialCostCreate, owner_id: int
    ) -> MaterialCost:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
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
