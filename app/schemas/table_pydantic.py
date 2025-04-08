"""Pydantic schemas for Table model."""

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
