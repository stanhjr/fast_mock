from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user import UserRepository
from schemas.user import UserSchemaAdd, UserSchemaLogin


class UserService:
    def __init__(self, user_repo: UserRepository, session: AsyncSession):
        self.user_repo: UserRepository = user_repo(session)

    async def add_user(self, user: UserSchemaAdd):
        user_dict = user.model_dump()
        user_id = await self.user_repo.add_one(user_dict)
        return user_id

    async def get_users(self):
        stocks = await self.user_repo.find_all()
        return stocks

    async def check_password(self, user: UserSchemaLogin) -> bool:
        user_dict = user.model_dump()
        is_checked = await self.user_repo.check_password(user_dict)
        return is_checked

    async def delete_user(self, user_id: UUID):
        user_id = await self.user_repo.delete_one(model_id=user_id)
        return user_id
