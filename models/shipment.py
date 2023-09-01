import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import Base
from models.mixins import GroupMixin
from schemas.enums import ShipmentStatusEnum

if TYPE_CHECKING:
    from models.order import Order
    from models.stock import Stock
    from models.image import ShipmentDocsPhoto


class Shipment(GroupMixin, Base):
    __tablename__ = "shipments"
    status: Mapped[ShipmentStatusEnum] = mapped_column(default=ShipmentStatusEnum.in_stock)

    order_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="shipments")
    stock_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("stocks.id"))
    stock: Mapped["Stock"] = relationship(back_populates="shipments")
    docs_photos: Mapped[list["ShipmentDocsPhoto"]] = relationship(back_populates="shipment")

    def __str__(self):
        return f"Shipment {self.status} order_id {self.order_id} stock {self.stock.name}"
