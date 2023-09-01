import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base
from models.mixins import ImageMixin

if TYPE_CHECKING:
    from models.item_model import Item


class ItemPhoto(ImageMixin, Base):
    __tablename__ = "item_photos"
    item_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("items.id"))
    item: Mapped["Item"] = relationship(back_populates="photos")


class UserPhoto(ImageMixin, Base):
    __tablename__ = "user_photos"
