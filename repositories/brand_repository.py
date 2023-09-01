from models.brand_model import Brand
from utils.repository import SQLAlchemyRepository


class BrandRepository(SQLAlchemyRepository):
    model = Brand


