from models.category_model import Category
from utils.repository import SQLAlchemyRepository


class CategoryRepository(SQLAlchemyRepository):
    model = Category
