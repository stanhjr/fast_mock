from uuid import UUID

from pydantic import BaseModel


class ItemSchema(BaseModel):
    width: int
    height: int
    price: int
    description: int
    brand_id: UUID
    sku_id: UUID
    category_id: UUID
    stock_id: UUID

    class Config:
        from_attributes = True


class ItemSchemaAdd(BaseModel):
    width: int
    height: int
    price: int
    description: int
    stock_id: UUID
    sku_id: UUID
