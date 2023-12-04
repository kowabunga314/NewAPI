from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from core.utilities import get_db
from supply.schema import MaterialCost, ProductionCost


router = APIRouter()

# Material costs

@router.get("/{supply_id}/", response_model=MaterialCost)
async def read_material_cost(*, db: Session = Depends(get_db), supply_id) -> Any:
    return None

@router.get("/", response_model=list[MaterialCost])
async def query_material_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.put("/", response_model=MaterialCost)
async def create_material_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.post("/", response_model=MaterialCost)
async def update_material_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.delete("/{supply_id}")
async def delete_material_cost(*, db: Session = Depends(get_db), supply_id) -> Any:
    return None


# Production Costs

@router.get("/{supply_id}/", response_model=ProductionCost)
async def read_production_cost(*, db: Session = Depends(get_db), supply_id) -> Any:
    return None

@router.get("/", response_model=list[ProductionCost])
async def query_production_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.put("/", response_model=ProductionCost)
async def create_production_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.post("/", response_model=ProductionCost)
async def update_production_cost(*, db: Session = Depends(get_db)) -> Any:
    return None

@router.delete("/{supply_id}")
async def delete_production_cost(*, db: Session = Depends(get_db), supply_id) -> Any:
    return None