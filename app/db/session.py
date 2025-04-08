"""Session and sessionmaker setup."""

from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.engine import engine

new_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
