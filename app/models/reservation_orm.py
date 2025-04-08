"""SQLAlchemy model for table reservations."""

from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_orm import Base


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
