from sqlalchemy import ForeignKey

from models.base_model import Base
import uuid

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING
from models.mixins import GroupMixin

if TYPE_CHECKING:
    from models.stock_model import Stock
    from models.category_model import Category
    from models.brand_model import Base
    from models.image_model import ItemPhoto
    from models.brand_model import Brand
    from models.shipment_item_model import ShipmentItem


class Item(GroupMixin, Base):
    __tablename__ = "items"
    brand_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("brands.id"))
    brand: Mapped["Brand"] = relationship(back_populates="items")
    category_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="items")
    stock_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("stocks.id"), nullable=True)
    stock: Mapped["Stock"] = relationship(back_populates="items")
    photos: Mapped[list["ItemPhoto"]] = relationship(back_populates="item")
    shipment_item: Mapped[list["ShipmentItem"]] = relationship(back_populates="item")
    sku: Mapped[str]
    description: Mapped[str | None]
    width:  Mapped[int]
    height: Mapped[int]
    price: Mapped[int]
    write_of: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"Item {self.sku}"
