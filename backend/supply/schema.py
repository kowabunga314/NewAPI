from pydantic import Field, HttpUrl

from core.schema import BaseItem, BaseItemBase
from . import CostFactorType


class CostFactorBase(BaseItemBase):
    """
    CostFactorBase basic cost factor class

    Contains most of the basic fields for cost factors, but excludes any values which are generated when a record is 
    inserted into the database.
    """
    type: CostFactorType


class CostFactor(BaseItem, CostFactorBase):
    """
    CostFactor full cost factor class

    Contains all information required to represent the CostFactor model.
    """
    pass

    class Config:
        from_attributes = True


class MaterialCostBase(CostFactorBase):
    cost: float = Field(ge=0, description="The price must be greater than or equal to zero")
    url: HttpUrl = None

    def __init__(self):
        self.type = CostFactorType.MATERIAL


class MaterialCost(MaterialCostBase, CostFactor):
    pass

    class Config:
        from_attributes = True


class ProductionCostBase(CostFactorBase):
    magnitude: float = Field(gt=0, lt=1, description="The magnitude of the cost factor must be between 0 and 1")

    def __init__(self):
        self.type = CostFactorType.PRODUCTION


class ProductionCost(ProductionCostBase, CostFactor):
    pass

    class Config:
        from_attributes = True
