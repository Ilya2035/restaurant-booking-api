from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.pydantic_models import ReservationResponse, ReservationCreate
from app.db.dependency import get_session
from app.models.orm_models import Reservation
from app.crud.transactions import create_records, list_of_records, delete_record

router_reservations = APIRouter(prefix="/reservations", tags=["reservations"])


@router_reservations.post("/", response_model=ReservationResponse, status_code=201)
async def table_create(data: ReservationCreate, db: AsyncSession = Depends(get_session)):
    return await create_records(Reservation, db, **data.dict())


@router_reservations.get("/", response_model=list[ReservationResponse])
async def table_list(db: AsyncSession = Depends(get_session)):
    return await list_of_records(Reservation, db)


@router_reservations.delete("/{id}", status_code=200)
async def table_delete(id: int, db: AsyncSession = Depends(get_session)):
    await delete_record(Reservation, db, id)
