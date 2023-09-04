from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstract import AbstractRepository
from schemas.item import ItemSchema


class ItemService:
    def __init__(self, item_repo: AbstractRepository, session: AsyncSession):
        self.item_repo: AbstractRepository = item_repo(session)

    async def add_item(self, item: ItemSchema):
        items_dict = item.model_dump()
        item_id = await self.item_repo.add_one(items_dict)
        return item_id

    async def get_items(self):
        items = await self.item_repo.find_all()
        return items
