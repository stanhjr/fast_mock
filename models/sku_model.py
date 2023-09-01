import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base

from models.mixins import GroupMixin
from schemas.sku import SkuSchema

if TYPE_CHECKING:
    from models.brand_model import Brand
    from models.category_model import Category


class Sku(GroupMixin, Base):
    __tablename__ = "sku"
    __table_args__ = (
        UniqueConstraint("brand_id", "category_id", "sku", name="sku_constraint"),
    )
    brand_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("brands.id"))
    brand: Mapped["Brand"] = relationship(back_populates="sku_list")
    category_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="sku_list")
    sku: Mapped[str | None] = mapped_column(unique=True, index=True)
    description: Mapped[str | None]
    weight: Mapped[int]
    base_price: Mapped[int]

    def __str__(self):
        return f"SKU {self.sku}"

    def to_read_model(self) -> SkuSchema:
        return SkuSchema(
            id=self.id,
            group_id=self.group_id,
            brand_id=self.brand_id,
            category_id=self.category_id,
            description=self.description,
            sku=self.sku,
            weight=self.weight,
            base_price=self.base_price,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
