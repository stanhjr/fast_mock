from models.brand import Brand
from repositories.abstract import SQLAlchemyRepository


class BrandRepository(SQLAlchemyRepository):
    model = Brand


