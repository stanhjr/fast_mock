import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from schemas.enums import PlaceTypeEnum


class GroupMixin:
    group_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("groups.id"))

    @declared_attr
    def group(self) -> Mapped["Group"]:
        return relationship("Group")


class PlaceMixin:
    address: Mapped[str]
    type: Mapped[PlaceTypeEnum] = mapped_column(default=PlaceTypeEnum.prime)
    owner_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("users.id"))

    @declared_attr
    def owner(self) -> Mapped["User"]:
        return relationship("User")


class ImageMixin:
    link: Mapped[str]


author_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("users.id"), nullable=True)
