import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base_model import Base
from models.mixins import GroupMixin
from schemas.enums_schema import ShipmentStatusEnum


class Shipment(GroupMixin, Base):
    __tablename__ = "shipments"
    order_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="shipments")
    stock_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("stocks.id"))
    stock: Mapped["Stock"] = relationship(back_populates="shipments")
    status: Mapped[ShipmentStatusEnum] = mapped_column(default=ShipmentStatusEnum.in_stock)

    def __str__(self):
        return f"Shipment {self.status} order_id {self.order_id} stock {self.stock.name}"
