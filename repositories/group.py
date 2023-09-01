from models.group_model import Group
from utils.repository import SQLAlchemyRepository


class GroupRepository(SQLAlchemyRepository):
    model = Group
