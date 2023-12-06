from pydantic import BaseModel, Field


class BaseItemBase(BaseModel):
    name: str = Field(index=True)
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    tags: set[str] = None


class BaseItem(BaseItemBase):
    id: int = Field(unique=True, index=True)
    owner_id: int
