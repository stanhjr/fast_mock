import uuid

from pydantic import BaseModel


class ItemSchema(BaseModel):
    brand_id: uuid.uuid4
    category_id: uuid.uuid4
    stock_id: uuid.uuid4
    sku: str
    width: int
    height: int
    assignee_id: int

    class Config:
        from_attributes = True
