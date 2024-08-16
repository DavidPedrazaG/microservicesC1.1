from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse
from .routes.user import user_route

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(user_route, prefix="/events", tags=["Eventos"])
app.include_router(user_route, prefix="/locations", tags=["Localidad"])
app.include_router(user_route, prefix="/orders", tags=["Order"])