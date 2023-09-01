import uuid

from sqlalchemy import ForeignKey

from models.base_model import Base
from models.mixins import GroupMixin
from schemas.enums_schema import UserRoleEnum
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column


class User(GroupMixin, Base):
    __tablename__ = "users"
    first_name: Mapped[str]
    last_name: Mapped[str]
    user_name: Mapped[str] = mapped_column(unique=True)
    last_login: Mapped[datetime | None]
    role: Mapped[UserRoleEnum] = mapped_column(default=UserRoleEnum.other)
    phone: Mapped[str | None]
    hashed_password: Mapped[str]
    avatar_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("user_photos.id"))
    avatar: Mapped["UserPhoto"] = relationship()

    def __str__(self):
        return f"User {self.user_name}"
