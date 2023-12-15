# from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database.base_class import Base

# if TYPE_CHECKING:
    # from admin.models import User
from admin.models import User



class Item(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner: User = relationship("User", back_populates="items")
