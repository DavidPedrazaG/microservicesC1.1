from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse
from .routes.user import user_route
from .routes.order import order_route
from .routes.location import location_route
from .routes.event import event_route
from .routes.item import item_route

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(event_route, prefix="/events", tags=["Eventos"])
app.include_router(location_route, prefix="/locations", tags=["Localidad"])
app.include_router(order_route, prefix="/orders", tags=["Order"])
app.include_router(item_route, prefix="/orders", tags=["Order"])