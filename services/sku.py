from schemas.sku import SkuSchemaAdd
from repositories.abstract import AbstractRepository


class SkuService:
    def __init__(self, sku_repo: AbstractRepository):
        self.sku_repo: AbstractRepository = sku_repo()

    async def add_sku(self, sku: SkuSchemaAdd):
        sku_dict = sku.model_dump()
        sku_id = await self.sku_repo.add_one(sku_dict)
        return sku_id

    async def get_sku_list(self):
        sku_list = await self.sku_repo.find_all()
        return sku_list
