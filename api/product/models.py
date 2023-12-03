from api.models import BaseItem
from api.product import CostFactorType


class CostFactor(BaseItem):
    type: CostFactorType

class Product(BaseItem):
    profit_margin: float
    sku: str = None
    cost_factors: list[CostFactor]

class MaterialCost(CostFactor):
    type = CostFactorType.MATERIAL
    cost: int
    url: str

class ProductionCost(CostFactor):
    type = CostFactorType.PRODUCTION
    magnitude: float
