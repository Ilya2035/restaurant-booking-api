"""Database engine creation."""

from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "sqlite+aiosqlite:///tronchecker.db",  # Заменишь на env-переменную позже
    echo=False,
)
