from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from supply.models import MaterialCost, ProductionCost
from database.base_class import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    profit_margin = Column(Float)
    sku = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    tags = Column(ARRAY(String))
    material_cost: MaterialCost = relationship(secondary='association_table')
    production_cost: ProductionCost = relationship(secondary='association_table')
