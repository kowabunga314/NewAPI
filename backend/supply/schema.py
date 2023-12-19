from pydantic import Field, HttpUrl

from core.schema import ItemBase, ItemInDBBase
from . import CostFactorType


class MaterialCostBase(ItemBase):
    cost: float = Field(ge=0, description="The price must be greater than or equal to zero")
    url: HttpUrl = None


class MaterialCostCreate(MaterialCostBase):
    pass


class MaterialCostUpdate(MaterialCostBase):
    pass


class MaterialCostInDBBase(ItemInDBBase, MaterialCostBase):

    class Config:
        from_attributes = True


class MaterialCost(MaterialCostInDBBase):
    pass


class ProductionCostBase(ItemBase):
    magnitude: float = Field(gt=0, description="The magnitude of the cost factor must be greater than 0")


class ProductionCostCreate(ProductionCostBase):
    pass


class ProductionCostUpdate(ProductionCostBase):
    pass


class ProductionCostInDBBase(ItemInDBBase, ProductionCostBase):

    class Config:
        from_attributes = True


class ProductionCost(ProductionCostInDBBase):
    pass
