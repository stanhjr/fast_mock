import bcrypt
from sqlalchemy import insert, select

from models.user import User
from repositories.abstract import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    salt = b'$2b$12$v1D5iA3NF/Qg3PT741qAg.'
    model = User

    async def _get_hashed_password(self, password: str) -> str:
        password = password.encode('utf-8')
        hashed_password_bytes = bcrypt.hashpw(password, self.salt)
        return hashed_password_bytes.decode('utf-8')

    async def _get_user_instance(self, username: str) -> User:
        stmt = select(self.model).where(
            self.model.username == username,
            self.model.is_deleted.is_(False),
            self.model.is_active.is_(True),
        )
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def check_password(self, data: dict) -> bool:
        user = await self._get_user_instance(
            username=data.get("username"),
        )
        if user.hashed_password == await self._get_hashed_password(password=data.get("password")):
            return True
        return False

    async def add_one(self, data: dict) -> int:
        hashed_password = await self._get_hashed_password(data.pop("password"))
        stmt = insert(self.model).values(hashed_password=hashed_password, **data).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()
