from typing import TypeVar, Type, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, text
from fastapi import HTTPException, status
from datetime import timedelta

from app.models.orm_models import Reservation

T = TypeVar('T')


async def create_records(model: Type[T], db: AsyncSession, **kwargs) -> T:
    instance = model(**kwargs)
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance


async def list_of_records(model: Type[T], db: AsyncSession) -> List[T]:
    result = await db.execute(select(model))
    return result.scalars().all()


async def delete_record(model_class: Type[T], db: AsyncSession, record_id: int) -> None:
    result = await db.execute(select(model_class).where(model_class.id == record_id))
    instance = result.scalar_one_or_none()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    await db.delete(instance)
    await db.commit()


async def create_record_reservation(db: AsyncSession, **kwargs):
    instance = Reservation(**kwargs)
    start_time = instance.reservation_time
    end_time = start_time + timedelta(minutes=instance.duration_minutes)

    query = select(Reservation).where(
        and_(
            Reservation.table_id == instance.table_id,
            Reservation.reservation_time < end_time,
            (Reservation.reservation_time + text(
                f"INTERVAL '{instance.duration_minutes} minutes'")) > start_time
        )
    )
    result = await db.execute(query)
    conflict = result.scalars().first()

    if conflict:
        raise ValueError("Столик уже забронирован на это время.")

    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance
