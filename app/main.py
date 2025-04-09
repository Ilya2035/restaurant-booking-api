from fastapi import FastAPI

from app.db.init import init_db
from app.api.table import router_table
from app.api.reservation import router_reservations

app = FastAPI(title="resturant_booking")


@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(router_table)
app.include_router(router_reservations)
