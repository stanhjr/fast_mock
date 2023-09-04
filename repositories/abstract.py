from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        pass

    @abstractmethod
    async def find_all(self):
        pass

    @abstractmethod
    async def delete_one(self, model_id: UUID):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession = None):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def get_by_id(self, model_id: UUID):
        stmt = select(self.model).where(
            self.model.is_deleted.is_(False),
            self.model.is_active.is_(True),
            self.model.id == model_id
        )
        res = await self.session.execute(stmt)
        row = res.fetchone()
        if row is not None:
            return row[0]

    async def find_all(self):
        stmt = select(self.model).where(
            self.model.is_deleted.is_(False),
            self.model.is_active.is_(True)
        )
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def delete_one(self, model_id: UUID):
        stmt = select(self.model).where(self.model.id == model_id).with_for_update()
        await self.session.execute(stmt)
        stmt = (
            update(self.model).
            where(self.model.id == model_id).
            values(is_deleted=True).
            returning(self.model.id)
        )
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()
