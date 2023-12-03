from pydantic import BaseModel, Field


class BaseItem(BaseModel):
    id: int
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    tags: set[str] = None