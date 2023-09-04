from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstract import AbstractRepository
from schemas.brand import BrandSchemaAdd


class CategoryService:
    def __init__(self, category_repo: AbstractRepository, session: AsyncSession):
        self.category_repo: AbstractRepository = category_repo(session)

    async def add_category(self, category: BrandSchemaAdd):
        category_dict = category.model_dump()
        category_repo_id = await self.category_repo.add_one(category_dict)
        return category_repo_id

    async def get_categories(self):
        categories = await self.category_repo.find_all()
        return categories
