from models.item import Item
from repositories.abstract import SQLAlchemyRepository


class ItemRepository(SQLAlchemyRepository):
    model = Item
