from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.base_class import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    profit_margin = Column(Float)
    sku = Column(String)

    tags = relationship("Tag")
    cost_factors = relationship("CostFactor")