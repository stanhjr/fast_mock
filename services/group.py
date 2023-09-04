from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstract import AbstractRepository
from schemas.brand import BrandSchemaAdd


class GroupService:
    def __init__(self, group_repo: AbstractRepository, session: AsyncSession):
        self.group_repo: AbstractRepository = group_repo(session)

    async def add_group(self, group: BrandSchemaAdd):
        group_dict = group.model_dump()
        group_id = await self.group_repo.add_one(group_dict)
        return group_id

    async def get_groups(self):
        groups = await self.group_repo.find_all()
        return groups

