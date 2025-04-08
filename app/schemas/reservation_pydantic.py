"""Pydantic schemas for Reservation model."""

from datetime import datetime

from pydantic import BaseModel, Field


class ReservationBase(BaseModel):
    customer_name: str = Field(..., example="Иван Иванов")
    table_id: int = Field(..., example=1)
    reservation_time: datetime = Field(..., example="2025-04-08T19:00:00")
    duration_minutes: int = Field(..., gt=0, example=60)


class ReservationCreate(ReservationBase):
    """Schema for creating a new reservation."""
    pass


class ReservationResponse(ReservationBase):
    """Schema for returning reservation data."""
    id: int

    class Config:
        from_attributes = True
