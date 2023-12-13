from pydantic import Field, HttpUrl

from core.schema import BaseItem, BaseItemBase
from supply.schema import CostFactor


class ProductBase(BaseItemBase):
    profit_margin: float = Field(gt=0, lt=1, description="The profit margin must be between 0 and 1")
    sku: str = None
    cost_factors: list[CostFactor] = None


class ProductCreate(ProductBase):
    pass


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(BaseItem, ProductBase):

    class Config:
        from_attributes = True


class Product(ProductInDBBase):
    pass
