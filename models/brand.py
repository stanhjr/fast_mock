from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from schemas.brand import BrandSchema

if TYPE_CHECKING:
    from models.item import Item
    from models.sku import Sku


class Brand(Base):
    __tablename__ = "brands"
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]
    items: Mapped[list["Item"]] = relationship(back_populates="brand")
    sku_list: Mapped[list["Sku"]] = relationship(back_populates="brand")

    def __str__(self):
        return f"Brand {self.name}"

    def to_read_model(self) -> BrandSchema:
        return BrandSchema(
            id=self.id,
            name=self.name,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
