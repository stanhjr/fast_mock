import uuid

from sqlalchemy import insert, select

from models.item import Item
from models.sku import Sku
from repositories.abstract import SQLAlchemyRepository


class ItemRepository(SQLAlchemyRepository):
    model = Item
    sku_model = Sku

    async def _get_sku_instance(self, sku_id: uuid.uuid4) -> Sku:
        stmt = select(self.sku_model).where(Sku.id == sku_id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def add_one(self, data: dict) -> int:
        sku = await self._get_sku_instance(sku_id=data.get("sku_id"))
        stmt = insert(self.model).values(
            category_id=sku.category_id,
            brand_id=sku.brand_id,
            **data
        ).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model).where(
            self.model.is_deleted.is_(False),
            self.model.is_active.is_(True),
            self.model.write_of.is_(False)
        )
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
