from fastapi.encoders import jsonable_encoder
import json
import logging
from sqlalchemy.orm import Session
from typing import Any, Dict, List, Union

from core.crud import CRUDBase
from core.utilities import get_db
from product.models import Product, MaterialCost, ProductionCost
from product.schema import ProductById, ProductOut, ProductCreate, ProductUpdate, ProductInDBBase, MaterialCostById, MaterialCostCreate, MaterialCostUpdate, ProductionCostCreate, ProductionCostUpdate


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

        # Query material costs
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

    def update(
        self,
        db: Session,
        *,
        db_obj: ProductInDBBase,
        obj_in: Union[ProductUpdate, Dict[str, Any]]
    ) -> ProductOut:
        # Get current model instance in JSON-friendly format
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            # Get input data as dictionary while excluding any unset fields
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:  # Model instance fields
            if field in update_data:    # Match model instance fields to input data fields
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)

        # Add material costs if present
        if 'material_costs' in update_data:
            for mc in update_data['material_costs']:
                material_cost = db.query(MaterialCost).filter(MaterialCost.id == mc['id']).first()
                if not material_cost:
                    raise LookupError(f'Material Cost not found: ID {mc["id"]}')
                db_obj.material_costs.append(material_cost)

        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def delete_material_costs_from_product(
        self,
        db: Session,
        *,
        db_obj: ProductInDBBase,
        # obj_in: Union[ProductById, Dict[str, Any]],
        material_costs: list[MaterialCostById]
    ) -> ProductOut:
        # Get current model instance in JSON-friendly format
        obj_data = jsonable_encoder(db_obj)
        # if isinstance(obj_in, dict):
        #     update_data = obj_in
        # else:
        #     # Get input data as dictionary while excluding any unset fields
        #     update_data = obj_in.model_dump(exclude_unset=True)

        logger.info(f'Object data: {db_obj.material_costs}')

        # Regenerate material cost list without deleted material costs
        db_obj.material_costs = [mc for mc in db_obj.material_costs if mc.id not in [m.id for m in material_costs]]

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



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
