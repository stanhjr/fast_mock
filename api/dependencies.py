from repositories.brand_repository import BrandRepository
from repositories.category import CategoryRepository
from repositories.sku import SkuRepository
from repositories.group import GroupRepository

from services.brands import BrandService
from services.category import CategoryService
from services.sku import SkuService
from services.group import GroupService


def brand_service():
    return BrandService(BrandRepository)


def category_service():
    return CategoryService(CategoryRepository)


def sku_service():
    return SkuService(SkuRepository)


def group_service():
    return GroupService(GroupRepository)
