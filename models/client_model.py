import uuid
from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import ForeignKey

from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.mixins import GroupMixin
from models.shop_model import Shop


class Client(GroupMixin, Base):
    __tablename__ = "clients"
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str | None]
    address: Mapped[str | None]
    shop_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("shops.id"))
    shop: Mapped["Shop"] = relationship(back_populates="clients")

    def __str__(self):
        return f"client {self.first_name} {self.last_name}"
