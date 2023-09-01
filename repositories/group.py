from models.group import Group
from repositories.abstract import SQLAlchemyRepository


class GroupRepository(SQLAlchemyRepository):
    model = Group
