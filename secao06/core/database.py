from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

session_local = sessionmaker(
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
    bind=engine,
)