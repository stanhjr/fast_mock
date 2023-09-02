from models.stock import Stock
from repositories.abstract import SQLAlchemyRepository


class StockRepository(SQLAlchemyRepository):
    model = Stock
