from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import Mapped, mapped_column,relationship

from admin.models import User
from core.models import Item
from database.base_class import Base
from supply.models import MaterialCost, ProductionCost


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


class Product(Item):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(ForeignKey("item.id"), primary_key=True)
    profit_margin = Column(Float)
    sku = Column(String)
    tags = Column(ARRAY(String))
    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner: Mapped[User] = relationship("User", back_populates="products")
    # material_costs: Mapped[MaterialCost] = relationship(secondary='product_material_cost')
    # production_costs: Mapped[ProductionCost] = relationship(secondary='product_production_cost')
