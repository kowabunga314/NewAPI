from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List

from admin.crud import user as user_crud
from admin.models import User
from core.utilities import get_current_active_user, get_db
from product.crud import product as product_crud
from product.schema import Product, ProductCreate, ProductUpdate


router = APIRouter()


@router.get("/", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Product = Depends(get_current_active_user),
) -> Any:
    """
    Retrieve products.
    """
    if user_crud.is_superuser(current_user):
        products = product_crud.get_multi(db, skip=skip, limit=limit)
    else:
        products = product_crud.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return products


@router.post("/", response_model=Product)
def create_product(
    *,
    db: Session = Depends(get_db),
    product_in: ProductCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new product.
    """
    product = product_crud.create_with_owner(db=db, obj_in=product_in, owner_id=current_user.id)
    return product


@router.put("/{id}", response_model=Product)
def update_product(
    *,
    db: Session = Depends(get_db),
    id: int,
    product_in: ProductUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update a product.
    """
    product = product_crud.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not user_crud.is_superuser(current_user) and (product.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    product = product_crud.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.get("/{id}", response_model=Product)
def read_product(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get product by ID.
    """
    product = product_crud.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not user_crud.is_superuser(current_user) and (product.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return product


@router.delete("/{id}", response_model=Product)
def delete_product(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Delete a product.
    """
    product = product_crud.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not user_crud.is_superuser(current_user) and (product.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    product = product_crud.remove(db=db, id=id)
    return product
