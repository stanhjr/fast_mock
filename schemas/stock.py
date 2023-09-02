from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

from schemas.enums import PlaceTypeEnum


class StockSchema(BaseModel):
    id: UUID
    name: str
    address: str
    owner_id: UUID
    type: PlaceTypeEnum
    group_id: UUID
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class StockSchemaAdd(BaseModel):
    group_id: UUID
    name: str
    type: PlaceTypeEnum
    address: str
    owner_id: UUID
