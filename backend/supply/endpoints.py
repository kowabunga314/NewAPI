from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any

from admin.crud import user as user_crud
from admin.models import User
from core.utilities import get_current_active_user, get_db
from supply.crud import material_cost as material_cost_crud, production_cost as production_cost_crud
from supply.schema import (
    MaterialCost, MaterialCostCreate, MaterialCostUpdate,
    ProductionCost, ProductionCostCreate, ProductionCostUpdate
)


router = APIRouter()

# Material costs

@router.get("/material-cost/{supply_id}/", response_model=MaterialCost)
async def read_material_cost(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    if user_crud.is_superuser(current_user):
        material_costs = material_cost_crud.get_multi(db, skip=skip, limit=limit)
    else:
        material_costs = material_cost_crud.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)
    return material_costs

@router.put("/material-cost/", response_model=MaterialCost)
async def create_material_cost(
    *,
    db: Session = Depends(get_db),
    material_cost_in: MaterialCostCreate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    create_material_cost Creates a new material cost

    Use this endpoint to generate a new material cost

    Args:
        material_cost_in (MaterialCostCreate): MaterialCostCreate schema
        db (Session, optional): Database session. Defaults to Depends(get_db).
        current_user (User, optional): The user to own the material cost. Defaults to Depends(get_current_active_user).

    Returns:
        Any: Returns a material cost
    """
    material_cost = material_cost_crud.create_with_owner(db=db, obj_in=material_cost_in, owner_id=current_user.id)
    return material_cost

@router.post("/material-cost/", response_model=MaterialCost)
async def update_material_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    material_cost_in: MaterialCostUpdate,
    current_user: User, Depends(get_current_active_user),
) -> Any:
    material_cost = material_cost_crud.get(db=db, id=id)
    if not material_cost:
        raise HTTPException(status_code=404, detail="Material Cost not found")
    if not user_crud.is_superuser(current_user) and material_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    return material_cost

@router.get("/material-cost/{id}", response_model=list[MaterialCost])
async def read_material_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    material_cost = material_cost_crud.get(db=db, id=id)
    if not material_cost:
        raise HTTPException(status_code=404, detail="Material Cost not found")
    if not user_crud.is_superuser(current_user) and material_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    return material_cost

@router.delete("/material-cost/{supply_id}")
async def delete_material_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    material_cost = material_cost_crud.get(db=db, id=id)
    if not material_cost:
        raise HTTPException(status_code=404, detail="Material Cost not found")
    if not user_crud.is_superuser(current_user) and material_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    material_cost = material_cost_crud.remove(db=db, id=id)
    return material_cost


# Production Costs

@router.get("/production-cost/{supply_id}/", response_model=ProductionCost)
async def read_production_cost(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    if user_crud.is_superuser(current_user):
        production_costs = production_cost_crud.get_multi(db, skip=skip, limit=limit)
    else:
        production_costs = production_cost_crud.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)
    return production_costs

@router.put("/production-cost/", response_model=ProductionCost)
async def create_production_cost(
    *,
    db: Session = Depends(get_db),
    production_cost_in: ProductionCostCreate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    create_production_cost Creates a new production cost

    Use this endpoint to generate a new production cost

    Args:
        production_cost_in (ProductionCostCreate): ProductionCostCreate schema
        db (Session, optional): Database session. Defaults to Depends(get_db).
        current_user (User, optional): The user to own the production cost. Defaults to Depends(get_current_active_user).

    Returns:
        Any: Returns a production cost
    """
    production_cost = production_cost_crud.create_with_owner(db=db, obj_in=production_cost_in, owner_id=current_user.id)
    return production_cost

@router.post("/production-cost/", response_model=ProductionCost)
async def update_production_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    production_cost_in: ProductionCostUpdate,
    current_user: User, Depends(get_current_active_user),
) -> Any:
    production_cost = production_cost_crud.get(db=db, id=id)
    if not production_cost:
        raise HTTPException(status_code=404, detail="Production Cost not found")
    if not user_crud.is_superuser(current_user) and production_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    return production_cost

@router.get("/production-cost/{id}", response_model=list[ProductionCost])
async def read_production_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    production_cost = production_cost_crud.get(db=db, id=id)
    if not production_cost:
        raise HTTPException(status_code=404, detail="Production Cost not found")
    if not user_crud.is_superuser(current_user) and production_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    return production_cost

@router.delete("/production-cost/{supply_id}")
async def delete_production_cost(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    production_cost = production_cost_crud.get(db=db, id=id)
    if not production_cost:
        raise HTTPException(status_code=404, detail="Production Cost not found")
    if not user_crud.is_superuser(current_user) and production_cost.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="User is not authorized to perform this action.")
    production_cost = production_cost_crud.remove(db=db, id=id)
    return production_cost