from pydantic import BaseModel
from models.event_schema import Event
from models.location_schema import Location

class Item(BaseModel):
    id:str
    event:Event
    location:Location
    amount:int
    unit_price:float
