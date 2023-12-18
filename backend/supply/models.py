from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, ARRAY, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from admin.models import User
from database.base_class import Base



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
    # owner: Mapped[User] = relationship("User", back_populates="material_costs")
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