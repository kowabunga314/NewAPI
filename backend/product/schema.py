from pydantic import Field, HttpUrl

from core.schema import BaseItem, BaseItemBase
from supply.schema import CostFactor


class ProductBase(BaseItemBase):
    profit_margin: float = Field(gt=0, lt=1, description="The profit margin must be between 0 and 1")
    sku: str = None
    cost_factors: list[CostFactor] = None


class ProductCreate(ProductBase):
    pass


class Product(BaseItem, ProductBase):
    pass

    class Config:
        from_attributes = True
