from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from routes.user import user_route
from routes.event import event_route
from routes.item import item_route
from routes.order import order_route
from routes.location import location_route

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()

    try:
        yield

    finally:
        if not connection.is_closed():
            connection.close

app = FastAPI(lifespan = lifespan)

app.include_router(user_route, prefix="/users", tags={"users"})
app.include_router(event_route, prefix="/event", tags={"events"})
app.include_router(item_route, prefix="/item", tags={"items"})
app.include_router(order_route, prefix="/order", tags={"orders"})
app.include_router(location_route, prefix="/location", tags={"locations"})