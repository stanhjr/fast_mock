from sqlalchemy.ext.asyncio import AsyncSession

from repositories.sku import SkuRepository
from schemas.sku import SkuSchemaAdd


class SkuService:
    def __init__(self, sku_repo: SkuRepository, session: AsyncSession):
        self.sku_repo: SkuRepository = sku_repo(session)

    async def add_sku(self, sku: SkuSchemaAdd):
        sku_dict = sku.model_dump()
        sku_id = await self.sku_repo.add_one(sku_dict)
        return sku_id

    async def get_sku_list(self):
        sku_list = await self.sku_repo.find_all()
        return sku_list
