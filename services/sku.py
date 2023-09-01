from schemas.sku import SkuSchemaAdd
from utils.repository import AbstractRepository


class SkuService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add_sku(self, sku: SkuSchemaAdd):
        sku_dict = sku.model_dump()
        sku_id = await self.tasks_repo.add_one(sku_dict)
        return sku_id

    async def get_sku_list(self):
        sku_list = await self.tasks_repo.find_all()
        return sku_list
