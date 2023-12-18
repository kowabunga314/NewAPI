from pydantic import Field, HttpUrl

from core.schema import ItemInDBBase, ItemBase
from supply.schema import MaterialCostBase, ProductionCostBase


class ProductBase(ItemBase):
    profit_margin: float = Field(gt=0, default=0.45, description="The profit margin must be between 0 and 1")
    sku: str = None
    # material_costs: list[MaterialCostBase] = None
    # production_costs: list[ProductionCostBase] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ItemInDBBase, ProductBase):

    class Config:
        from_attributes = True


class Product(ProductInDBBase):
    pass
