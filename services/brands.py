from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.brand import BrandRepository
from schemas.brand import BrandSchemaAdd


class BrandService:
    def __init__(self, brand_repo: BrandRepository, session: AsyncSession):
        self.brand_repo: BrandRepository = brand_repo(session)

    async def add_brand(self, brand: BrandSchemaAdd):
        brand_dict = brand.model_dump()
        brand_id = await self.brand_repo.add_one(brand_dict)
        return brand_id

    async def get_brands(self):
        brands = await self.brand_repo.find_all()
        return brands

    async def delete_brand(self, brand_id: UUID):
        brand_id = await self.brand_repo.delete_one(model_id=brand_id)
        return brand_id
