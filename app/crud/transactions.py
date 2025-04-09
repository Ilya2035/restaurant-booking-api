from typing import TypeVar, Type, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

T = TypeVar('T')


async def create_records(model: Type[T], db: AsyncSession, **kwargs) -> T:
    instance = model(**kwargs)
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance


async def list_of_records(model_class: Type[T], db: AsyncSession) -> List[T]:
    result = await db.execute(select(model_class))
    return result.scalars().all()


async def delete_record(model_class: Type[T], db: AsyncSession, record_id: int) -> None:
    result = await db.execute(select(model_class).where(model_class.id == record_id))
    instance = result.scalar_one_or_none()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    await db.delete(instance)
    await db.commit()
