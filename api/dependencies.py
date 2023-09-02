from repositories.brand import BrandRepository
from repositories.category import CategoryRepository
from repositories.group import GroupRepository
from repositories.item import ItemRepository
from repositories.sku import SkuRepository
from repositories.stock import StockRepository
from repositories.user import UserRepository
from services.brands import BrandService
from services.category import CategoryService
from services.group import GroupService
from services.item import ItemService
from services.sku import SkuService
from services.stock import StockService
from services.user import UserService


def user_service():
    return UserService(UserRepository)


def brand_service():
    return BrandService(BrandRepository)


def category_service():
    return CategoryService(CategoryRepository)


def sku_service():
    return SkuService(SkuRepository)


def group_service():
    return GroupService(GroupRepository)


def stock_service():
    return StockService(StockRepository)


def item_service():
    return ItemService(ItemRepository)
