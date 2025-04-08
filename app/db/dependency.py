"""Session dependency for FastAPI."""

from app.db.session import new_session


async def get_session():
    """Async DB session dependency."""
    async with new_session() as session:
        yield session
