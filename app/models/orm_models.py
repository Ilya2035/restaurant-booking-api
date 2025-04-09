from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

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


class Reservation(Base):
    """Model for storing table reservations."""
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column(nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id", ondelete="CASCADE"), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(nullable=False)

    table = relationship("Table", backref="reservations")

    def __repr__(self) -> str:
        return (
            f"<Reservation(id={self.id}, customer='{self.customer_name}', "
            f"table_id={self.table_id}, time={self.reservation_time}, "
            f"duration={self.duration_minutes})>"
        )
