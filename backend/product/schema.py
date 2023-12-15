from pydantic import Field, HttpUrl

from core.schema import ItemInDBBase, ItemBase
from supply.schema import CostFactor


class ProductBase(ItemBase):
    profit_margin: float = Field(gt=0, lt=1, description="The profit margin must be between 0 and 1")
    sku: str = None
    cost_factors: list[CostFactor] = None


class ProductCreate(ProductBase):
    pass


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ItemInDBBase, ProductBase):

    class Config:
        from_attributes = True


class Product(ProductInDBBase):
    pass
