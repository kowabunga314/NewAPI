from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.base_class import Base


class MaterialCost(Base):
    __tablename__ = "material_cost"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    type = Column(String)
    cost = Column(Float)
    url = Column(String)

    # tags = relationship("Tag")


class ProductionCost(Base):
    __tablename__ = "production_cost"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    type = Column(Float)
    magnitude = Column(Float)

    # tags = relationship("Tag")