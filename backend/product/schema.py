from pydantic import Field, HttpUrl
from typing import Optional, Union

from core.schema import ItemInDBBase, ItemBase


# Base Schema #

class ProductBase(ItemBase):
    profit_margin: float = Field(gt=0, default=0.45, description="The profit margin must be between 0 and 1")
    sku: str = None

    class Config:
        orm_mode = True

class MaterialCostBase(ItemBase):
    cost: float = Field(ge=0, description="The price must be greater than or equal to zero", default=0)
    url: HttpUrl = None
    type: str = None

    class Config:
        orm_mode = True

class ProductionCostBase(ItemBase):
    magnitude: float = Field(gt=0, description="The magnitude of the cost factor must be greater than 0")


# Products #
    
class ProductOutMinimal(ProductBase):
    id: int


class ProductOut(ProductOutMinimal):
    material_costs: list['MaterialCostOutMinimal']
    # production_costs: list[ProductionCostBase] = None


class ProductCreate(ProductBase):
    material_costs: Optional[list['MaterialCostOutMinimal']]


class ProductUpdate(ProductBase):
    id: int
    material_costs: Optional[list['MaterialCostOutMinimal']]


class ProductInDBBase(ItemInDBBase, ProductBase):
    id: int
    owner_id: int
    material_costs: list['MaterialCostOutMinimal']

    class Config:
        from_attributes = True


class Product(ProductInDBBase):
    pass


# Material Costs #

class MaterialCostOutMinimal(MaterialCostBase):
    id: int


class MaterialCostOut(MaterialCostOutMinimal):
    products: list['ProductOutMinimal']

class MaterialCostCreate(MaterialCostBase):
    pass


class MaterialCostUpdate(MaterialCostBase):
    id: int


class MaterialCostInDBBase(ItemInDBBase, MaterialCostBase):
    id: int
    products: list[ProductBase]

    class Config:
        from_attributes = True


class MaterialCost(MaterialCostInDBBase):
    pass


# Production Costs #


class ProductionCostCreate(ProductionCostBase):
    pass


class ProductionCostUpdate(ProductionCostBase):
    pass


class ProductionCostInDBBase(ItemInDBBase, ProductionCostBase):

    class Config:
        from_attributes = True


class ProductionCost(ProductionCostInDBBase):
    pass


ProductOut.model_rebuild()
ProductCreate.model_rebuild()
ProductUpdate.model_rebuild()
ProductInDBBase.model_rebuild()
MaterialCostOut.model_rebuild()
