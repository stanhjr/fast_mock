from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import GroupMixin
from schemas.enums import ShopStatusEnum


class Shop(GroupMixin, Base):
    __tablename__ = "shops"
    name: Mapped[str]
    destination: Mapped[str | None]
    status: Mapped[ShopStatusEnum] = mapped_column(default=ShopStatusEnum.open)

    api_key: Mapped[str | None] = mapped_column(unique=True, index=True)
    clients: Mapped[list["Client"]] = relationship(back_populates="shop")
    orders: Mapped[list["Order"]] = relationship(back_populates="shop")

    def __str__(self):
        return f"shop {self.name} {self.status}"
