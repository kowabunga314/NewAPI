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
    cost: float = Field(ge=0, description="The price must be greater than or equal to zero")
    url: HttpUrl = None
    type: str = None

    class Config:
        orm_mode = True

class ProductionCostBase(ItemBase):
    magnitude: float = Field(gt=0, description="The magnitude of the cost factor must be greater than 0")


# Products #

class ProductOut(ProductBase):
    material_costs: list[MaterialCostBase]
    # production_costs: list[ProductionCostBase] = None


class ProductCreate(ProductBase):
    material_costs: Optional[Union[list[int], list[MaterialCostBase]]]


class ProductAPICreate(ProductBase):
    material_costs: Optional[Union[list[int], list[MaterialCostBase]]]


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ItemInDBBase, ProductBase):
    owner_id: int
    material_costs: list[int]

    class Config:
        from_attributes = True


class Product(ProductInDBBase):
    pass

# Material Costs #


class MaterialCostOut(MaterialCostBase):
    products: 'list[ProductBase]' = []


class MaterialCostCreate(MaterialCostBase):
    pass


class MaterialCostUpdate(MaterialCostBase):
    pass


class MaterialCostInDBBase(ItemInDBBase, MaterialCostBase):

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


from product.schema import ProductBase
ProductBase.model_rebuild()
