from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from admin.models import User
from database.base_class import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    profit_margin = Column(Float)
    sku = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))