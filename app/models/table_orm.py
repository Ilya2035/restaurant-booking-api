"""SQLAlchemy model for restaurant tables."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_orm import Base


class Table(Base):
    """Model for storing restaurant tables."""
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    seats: Mapped[int] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Table(id={self.id}, name='{self.name}', "
            f"seats={self.seats}, location='{self.location}')>"
        )
