from repositories.abstract import AbstractRepository
from schemas.stock import StockSchemaAdd


class StockService:
    def __init__(self, stock_repo: AbstractRepository):
        self.stock_repo: AbstractRepository = stock_repo()

    async def add_stock(self, task: StockSchemaAdd):
        stock_dict = task.model_dump()
        stock_id = await self.stock_repo.add_one(stock_dict)
        return stock_id

    async def get_stocks(self):
        stocks = await self.stock_repo.find_all()
        return stocks
