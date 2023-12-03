from pydantic import BaseModel


class BaseItem(BaseModel):
    name: str
    description: str = None
    tags: list[str] = None