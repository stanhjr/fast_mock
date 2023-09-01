from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class GroupSchema(BaseModel):
    id: UUID
    group_id: int
    description: str

    class Config:
        from_attributes = True


class GroupSchemaAdd(BaseModel):
    group_id: int
    description: str
