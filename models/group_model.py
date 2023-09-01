from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from models.base_model import Base
from schemas.group import GroupSchema


class Group(Base):
    __tablename__ = "groups"
    group_id: Mapped[int] = mapped_column(unique=True)
    description: Mapped[str]

    def __str__(self):
        return f"Group {self.group_id}"

    def to_read_model(self) -> GroupSchema:
        return GroupSchema(
            id=self.id,
            group_id=self.group_id,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
