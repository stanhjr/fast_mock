import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import ImageMixin

if TYPE_CHECKING:
    from models.item import Item
    from models.shipment import Shipment
    from models.user import User


class ItemPhoto(ImageMixin, Base):
    __tablename__ = "item_photos"
    item_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("items.id"))
    item: Mapped["Item"] = relationship(back_populates="photos")


class UserPhoto(ImageMixin, Base):
    __tablename__ = "user_photos"
    user_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="photos")


class ShipmentDocsPhoto(ImageMixin, Base):
    __tablename__ = "shipment_docs_photos"
    shipment_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("shipments.id"))
    shipment: Mapped["Shipment"] = relationship(back_populates="docs_photos")
    upload_at: Mapped[datetime] = mapped_column(nullable=True)

    def __str__(self):
        return f"ShipmentDocsPhoto {self.shipment_id} upload_at {self.upload_at}"
