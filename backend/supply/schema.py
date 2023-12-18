from pydantic import Field, HttpUrl

from core.schema import ItemBase, ItemInDBBase
from . import CostFactorType


class CostFactorBase(ItemBase):
    """
    CostFactorBase basic cost factor class

    Contains most of the basic fields for cost factors, but excludes any values which are generated when a record is 
    inserted into the database.
    """
    type: CostFactorType


class CostFactor(CostFactorBase):
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


class MaterialCostCreate(MaterialCostBase):
    pass


class MaterialCostUpdate(MaterialCostBase):
    pass


class MaterialCostInDBBase(ItemInDBBase, MaterialCostBase):

    class Config:
        from_attributes = True


class MaterialCost(MaterialCostBase):
    pass


class ProductionCostBase(CostFactorBase):
    magnitude: float = Field(gt=0, description="The magnitude of the cost factor must be greater than 0")

    def __init__(self):
        self.type = CostFactorType.PRODUCTION


class ProductionCostCreate(ProductionCostBase):
    pass


class ProductionCostUpdate(ProductionCostBase):
    pass


class ProductionCostInDBBase(ItemInDBBase, ProductionCostBase):

    class Config:
        from_attributes = True


class ProductionCost(ProductionCostBase, CostFactor):
    pass
