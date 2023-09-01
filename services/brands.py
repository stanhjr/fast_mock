from schemas.brand import BrandSchemaAdd
from repositories.abstract import AbstractRepository


class BrandService:
    def __init__(self, brand_repo: AbstractRepository):
        self.brand_repo: AbstractRepository = brand_repo()

    async def add_brand(self, brand: BrandSchemaAdd):
        brand_dict = brand.model_dump()
        brand_id = await self.brand_repo.add_one(brand_dict)
        return brand_id

    async def get_brands(self):
        brands = await self.brand_repo.find_all()
        return brands

    async def delete_brand(self, brand_id: str):
        brand_id = await self.brand_repo.delete_one(model_id=brand_id)
        return brand_id
