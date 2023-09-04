from sqlalchemy.ext.asyncio import AsyncSession

from repositories.abstract import AbstractRepository
from schemas.stock import StockSchemaAdd


class StockService:
    def __init__(self, stock_repo: AbstractRepository, session: AsyncSession):
        self.stock_repo: AbstractRepository = stock_repo(session)

    async def add_stock(self, stock: StockSchemaAdd):
        stock_dict = stock.model_dump()
        stock_id = await self.stock_repo.add_one(stock_dict)
        return stock_id

    async def get_stocks(self):
        stocks = await self.stock_repo.find_all()
        return stocks
