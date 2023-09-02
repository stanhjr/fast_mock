from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from schemas.enums import UserRoleEnum


class UserSchema(BaseModel):
    id: UUID
    group_id: UUID
    first_name: str
    last_name: str
    user_name: str
    role: UserRoleEnum
    group_id: UUID
    last_login: datetime | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    phone: str
    password: str
    role: UserRoleEnum
    group_id: UUID


class UserSchemaLogin(BaseModel):
    username: str
    password: str
