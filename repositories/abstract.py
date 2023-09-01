from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        pass

    @abstractmethod
    async def find_all(self):
        pass

    @abstractmethod
    async def delete_one(self, model_id: str):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.is_deleted == False, self.model.is_active == True)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def delete_one(self, model_id: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == model_id).with_for_update()
            await session.execute(stmt)
            stmt = (
                update(self.model).
                where(self.model.id == model_id).
                values(is_deleted=True).
                returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
