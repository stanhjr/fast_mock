import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


if TYPE_CHECKING:
    from models.item import Item
    from models.stock import Stock


class ShipmentItem(Base):
    __tablename__ = "shipments_items"
    item_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("items.id"))
    item: Mapped["Item"] = relationship(back_populates="shipment_item")
    stock_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("stocks.id"))
    stock: Mapped["Stock"] = relationship(back_populates="shipment_item")
