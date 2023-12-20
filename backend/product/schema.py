from pydantic import Field, HttpUrl

from core.schema import ItemInDBBase, ItemBase


class ProductBase(ItemBase):
    profit_margin: float = Field(gt=0, default=0.45, description="The profit margin must be between 0 and 1")
    sku: str = None

    class Config:
        orm_mode = True


class ProductOut(ProductBase):
    material_costs: 'list[MaterialCostBase]' = []
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


from supply.schema import MaterialCostBase
MaterialCostBase.model_rebuild()