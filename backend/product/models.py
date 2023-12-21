from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import List

from admin.models import User
from database.base_class import Base


product_material_cost = Table('product_material_cost',
                    Base.metadata,
                    Column('product_id', Integer, ForeignKey('product.id')),
                    Column('material_cost_id', Integer, ForeignKey('material_cost.id'))
                    )

product_production_cost = Table('product_production_cost',
                    Base.metadata,
                    Column('product_id', Integer, ForeignKey('product.id')),
                    Column('production_cost_id', Integer, ForeignKey('production_cost.id'))
                    )

product_user = Table('product_user',
                    Base.metadata,
                    Column('product_id', Integer, ForeignKey('product.id')),
                    Column('user_id', Integer, ForeignKey('user.id'))
                    )


class Product(Base):
    __tablename__ = "product"

    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    profit_margin = Column(Float)
    sku = Column(String)
    tags = Column(ARRAY(String))
    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner: Mapped[User] = relationship("User", back_populates="products")
    material_costs: Mapped[List['MaterialCost']] = relationship(secondary='product_material_cost', back_populates='products')
    # production_costs: Mapped[ProductionCost] = relationship(secondary='product_production_cost')



material_cost_user = Table('material_cost_user',
                    Base.metadata,
                    Column('material_cost_id', Integer, ForeignKey('material_cost.id')),
                    Column('user_id', Integer, ForeignKey('user.id'))
                    )


production_cost_user = Table('production_cost_user',
                    Base.metadata,
                    Column('production_cost_id', Integer, ForeignKey('production_cost.id')),
                    Column('user_id', Integer, ForeignKey('user.id'))
                    )


class MaterialCost(Base):
    __tablename__ = "material_cost"

    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    type = Column(String)
    cost = Column(Float)
    url = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    products: Mapped[List[Product]] = relationship(secondary='product_material_cost', back_populates="material_costs")
    # owner: Mapped[User] = mapped_column(ForeignKey("item.owner"))

    # tags = relationship("Tag")


class ProductionCost(Base):
    __tablename__ = "production_cost"

    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    type = Column(Float)
    magnitude = Column(Float)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner: Mapped[User] = relationship("User", back_populates="production_costs")
    # owner: Mapped[User] = mapped_column(ForeignKey("item.owner"))

    # tags = relationship("Tag")