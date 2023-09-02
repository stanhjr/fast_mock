from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SkuSchema(BaseModel):
    id: UUID
    brand_id: UUID
    category_id: UUID
    weight: int
    base_price: int
    sku: str
    description: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class SkuSchemaAdd(BaseModel):
    brand_id: UUID
    group_id: UUID
    category_id: UUID
    weight: int
    base_price: int
