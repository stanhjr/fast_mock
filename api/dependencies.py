from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
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


def user_service(session: AsyncSession = Depends(get_async_session)):
    return UserService(UserRepository, session)


async def brand_service(session: AsyncSession = Depends(get_async_session)):
    return BrandService(BrandRepository, session)


def category_service(session: AsyncSession = Depends(get_async_session)):
    return CategoryService(CategoryRepository, session)


def sku_service(session: AsyncSession = Depends(get_async_session)):
    return SkuService(SkuRepository, session)


def group_service(session: AsyncSession = Depends(get_async_session)):
    return GroupService(GroupRepository, session)


def stock_service(session: AsyncSession = Depends(get_async_session)):
    return StockService(StockRepository, session)


def item_service(session: AsyncSession = Depends(get_async_session)):
    return ItemService(ItemRepository, session)
