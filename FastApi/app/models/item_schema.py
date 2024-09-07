from pydantic import BaseModel
from models.event_schema import Event
from models.location_schema import Location

class Item(BaseModel):
    id:int
    event_id:str
    location_id:str
    amount:int
    unit_price:float
