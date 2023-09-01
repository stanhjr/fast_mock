import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base
from models.mixins import GroupMixin

from schemas.enums_schema import OrderStatusEnum


class Order(GroupMixin, Base):
    __tablename__ = "orders"
    destination: Mapped[str]
    status: Mapped[OrderStatusEnum] = mapped_column(default=OrderStatusEnum.to_stock)
    shop_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("shops.id"))
    shop: Mapped["Shop"] = relationship(back_populates="orders")
    shipments: Mapped[list["Shipment"]] = relationship(back_populates="order")

    def __str__(self):
        return f"Order {self.status} {self.shop.name}"
