from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection

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