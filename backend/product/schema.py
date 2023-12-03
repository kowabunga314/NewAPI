from pydantic import Field, HttpUrl

from NewAPI.backend.api.schema import BaseItem, BaseItemBase
from backend.product import CostFactorType


class CostFactorBase(BaseItemBase):
    type: CostFactorType


class CostFactor(BaseItem, CostFactorBase):
    pass

    class Config:
        orm_mode = True

class ProductBase(BaseItemBase):
    profit_margin: float = Field(gt=0, lt=1, description="The profit margin must be between 0 and 1")
    sku: str = None
    cost_factors: list[CostFactor] = None


class Product(BaseItem, ProductBase):
    pass

    class Config:
        orm_mode = True


class MaterialCostBase(CostFactorBase):
    cost: float = Field(ge=0, description="The price must be greater than or equal to zero")
    url: HttpUrl = None

    def __init__(self):
        self.type = CostFactorType.MATERIAL


class MaterialCost(MaterialCostBase, CostFactor):
    pass

    class Config:
        orm_mode = True


class ProductionCostBase(CostFactorBase):
    magnitude: float = Field(gt=0, lt=1, description="The magnitude of the cost factor must be between 0 and 1")

    def __init__(self):
        self.type = CostFactorType.PRODUCTION


class ProductionCost(ProductionCostBase, CostFactor):
    pass

    class Config:
        orm_mode = True
