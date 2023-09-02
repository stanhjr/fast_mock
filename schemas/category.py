from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: UUID
    name: str
    description: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class CategorySchemaAdd(BaseModel):
    name: str
    description: str | None
