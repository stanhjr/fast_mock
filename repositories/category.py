from models.category import Category
from repositories.abstract import SQLAlchemyRepository


class CategoryRepository(SQLAlchemyRepository):
    model = Category
