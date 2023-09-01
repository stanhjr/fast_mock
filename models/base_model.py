import uuid

from datetime import datetime
from sqlalchemy import func, UUID, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: Mapped[uuid.uuid4] = mapped_column(UUID(as_uuid=True),
                                           primary_key=True,
                                           default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=datetime.now, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    author_id: Mapped[uuid.uuid4] = mapped_column(ForeignKey("users.id"))

    def __repr__(self):
        return str(self)
