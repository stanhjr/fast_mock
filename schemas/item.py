from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: UUID
    author_id: UUID | None
    width: int
    height: int
    price: int
    description: str
    brand_id: UUID
    sku_id: UUID
    category_id: UUID
    stock_id: UUID
    group_id: UUID
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True


class ItemSchemaAdd(BaseModel):
    width: int
    height: int
    price: int
    description: str
    stock_id: UUID
    sku_id: UUID
    group_id: UUID
