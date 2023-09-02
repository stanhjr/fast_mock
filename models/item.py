import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import GroupMixin
from schemas.item import ItemSchema

if TYPE_CHECKING:
    from models.brand import Base, Brand
    from models.category import Category
    from models.image import ItemPhoto
    from models.shipment_item import ShipmentItem
    from models.sku import Sku
    from models.stock import Stock


class Item(GroupMixin, Base):
    __tablename__ = "items"
    description: Mapped[str | None]
    width:  Mapped[int]
    height: Mapped[int]
    price: Mapped[int]
    write_of: Mapped[bool] = mapped_column(default=False)

    brand_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("brands.id"))
    brand: Mapped["Brand"] = relationship(back_populates="items")
    category_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="items")
    stock_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("stocks.id"), nullable=True)
    stock: Mapped["Stock"] = relationship(back_populates="items")
    photos: Mapped[list["ItemPhoto"]] = relationship(back_populates="item")
    shipment_item: Mapped[list["ShipmentItem"]] = relationship(back_populates="item")
    sku_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("sku.id"), nullable=True)
    sku: Mapped["Sku"] = relationship(back_populates="items")

    def __str__(self):
        return f"Item {self.sku_id}"

    def to_read_model(self) -> ItemSchema:
        return ItemSchema(
            id=self.id,
            width=self.width,
            height=self.height,
            brand_id=self.brand_id,
            category_id=self.category_id,
            stock_id=self.stock_id,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
