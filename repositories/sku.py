from sqlalchemy import insert, select

from db.db import async_session_maker
from models.brand import Brand
from models.category import Category
from models.sku import Sku
from repositories.abstract import SQLAlchemyRepository


class SkuRepository(SQLAlchemyRepository):
    model = Sku

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            category_stmt = select(Category.name).where(Category.id == data.get('category_id'))
            res = await session.execute(category_stmt)
            category_name = res.scalar_one()
            brand_stmt = select(Brand.name).where(Brand.id == data.get('brand_id'))
            res = await session.execute(brand_stmt)
            brand_name = res.scalar_one()
            data.update(sku=f"{category_name}_{brand_name}")
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model, Brand).join(self.model.brand)
            res = await session.execute(stmt)
            res = res.all()
            res = [row[0].to_read_model() for row in res]
            return res
