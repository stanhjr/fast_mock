from schemas.brands import BrandSchemaAdd
from utils.repository import AbstractRepository


class GroupService:
    def __init__(self, group_repo: AbstractRepository):
        self.group_repo: AbstractRepository = group_repo()

    async def add_group(self, task: BrandSchemaAdd):
        group_dict = task.model_dump()
        group_id = await self.group_repo.add_one(group_dict)
        return group_id

    async def get_groups(self):
        groups = await self.group_repo.find_all()
        return groups

