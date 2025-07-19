from collections.abc import AsyncGenerator

import redis.asyncio as redis
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from settings import Config
from models import Base
from models.users import User


DATABASE_URL = f"postgresql+asyncpg://{Config.Database.Postgres.database}:{Config.Database.Postgres.password}@{Config.Database.Postgres.host}:{Config.Database.Postgres.port}/{Config.Database.Postgres.database}"
REDIS_URL = f"redis://{Config.Database.Redis.host}:{Config.Database.Redis.port}/{Config.Database.Redis.db}"
REDIS = redis.from_url(REDIS_URL, decode_responses=True)  # idgaf

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
