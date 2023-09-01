from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from models.base_model import Base
from models.mixins import PlaceMixin

if TYPE_CHECKING:
    from models.item_model import Item
    from models.shipment_item_model import ShipmentItem
    from models.shipment_model import Shipment


class Stock(PlaceMixin, Base):
    __tablename__ = "stocks"
    name: Mapped[str]
    items: Mapped[list["Item"]] = relationship(back_populates="stock")
    shipments: Mapped[list["Shipment"]] = relationship(back_populates="stock")
    shipment_item: Mapped[list["ShipmentItem"]] = relationship(back_populates="stock")

    def __str__(self):
        return f"Stock type {self.type} {self.name}"
