from uuid import UUID

from pydantic import BaseModel

from schemas.enums import PlaceTypeEnum


class StockSchema(BaseModel):
    id: UUID
    name: str
    address: str
    description: str
    type: PlaceTypeEnum

    class Config:
        from_attributes = True


class StockSchemaAdd(BaseModel):
    group_id: int
    description: str
    type: PlaceTypeEnum | None
    address: str
    owner_id: UUID
