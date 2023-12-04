from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field


class BaseItemBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    tags: set[str] = None


class BaseItem(BaseItemBase):
    id: int = Field(unique=True, index=True)
    owner_id: int
