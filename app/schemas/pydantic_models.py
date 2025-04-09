from datetime import datetime

from pydantic import BaseModel, Field


class TableBase(BaseModel):
    name: str = Field(..., example="Table 1")
    seats: int = Field(..., gt=0, example=4)
    location: str = Field(..., example="у окна")


class TableCreate(TableBase):
    """Schema for creating a new table."""
    pass


class TableResponse(TableBase):
    """Schema for returning a table."""
    id: int

    class Config:
        from_attributes = True


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
