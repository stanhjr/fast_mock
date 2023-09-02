from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from models.base import Base
from models.mixins import PlaceMixin
from schemas.stock import StockSchema

if TYPE_CHECKING:
    from models.item import Item
    from models.shipment import Shipment
    from models.shipment_item import ShipmentItem


class Stock(PlaceMixin, Base):
    __tablename__ = "stocks"
    name: Mapped[str]

    items: Mapped[list["Item"]] = relationship(back_populates="stock")
    shipments: Mapped[list["Shipment"]] = relationship(back_populates="stock")
    shipment_item: Mapped[list["ShipmentItem"]] = relationship(back_populates="stock")

    def __str__(self):
        return f"Stock type {self.type} {self.name}"

    def to_read_model(self) -> StockSchema:
        return StockSchema(
            id=self.id,
            name=self.name,
            address=self.address,
            type=self.type,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
