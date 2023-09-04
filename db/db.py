from typing import Generator

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("postgresql+asyncpg://stan:postgres@localhost/all_stars")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> Generator:
    async with async_session_maker() as session:
        yield session
