from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BrandSchema(BaseModel):
    id: UUID
    name: str
    description: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class BrandSchemaAdd(BaseModel):
    name: str
    description: str | None
