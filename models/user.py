import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import GroupMixin
from schemas.enums import UserRoleEnum
from schemas.user import UserSchema

if TYPE_CHECKING:
    from models.image import UserPhoto


class User(GroupMixin, Base):
    __tablename__ = "users"
    first_name: Mapped[str]
    last_name: Mapped[str]
    user_name: Mapped[str] = mapped_column(unique=True)
    last_login: Mapped[datetime | None]
    role: Mapped[UserRoleEnum] = mapped_column(default=UserRoleEnum.other)
    phone: Mapped[str | None]
    hashed_password: Mapped[str]

    photos: Mapped["UserPhoto"] = relationship(back_populates="user")

    def __str__(self):
        return f"User {self.user_name}"

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            user_name=self.user_name,
            last_login=self.last_login,
            role=self.role,
            phone=self.phone,
            created_at=self.created_at,
            updated_at=self.updated_at,
            group_id=self.group_id,
        )
