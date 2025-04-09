from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.pydantic_models import TableResponse, TableCreate
from app.db.dependency import get_session
from app.models.orm_models import Table
from app.crud.transactions import create_records, list_of_records, delete_record

router_table = APIRouter(prefix="/tables", tags=["tables"])


@router_table.post("/", response_model=TableResponse, status_code=201)
async def table_create(data: TableCreate, db: AsyncSession = Depends(get_session)):
    return await create_records(Table, db, **data.dict())


@router_table.get("/", response_model=list[TableResponse])
async def table_list(db: AsyncSession = Depends(get_session)):
    return await list_of_records(Table, db)


@router_table.delete("/{id}", status_code=200)
async def table_delete(id: int, db: AsyncSession = Depends(get_session)):
    await delete_record(Table, db, id)
