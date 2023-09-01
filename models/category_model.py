from typing import TYPE_CHECKING

from models.base_model import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column

from schemas.category import CategorySchema

if TYPE_CHECKING:
    from models.item_model import Item
    from models.sku_model import Sku


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]
    items: Mapped[list["Item"]] = relationship(back_populates="category")
    sku_list: Mapped[list["Sku"]] = relationship(back_populates="category")

    def __str__(self):
        return f"Category {self.name}"

    def to_read_model(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
