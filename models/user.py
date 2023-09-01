import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from models.base import Base
from models.mixins import GroupMixin
from schemas.enums import UserRoleEnum
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

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
