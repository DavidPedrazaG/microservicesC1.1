from pydantic import BaseModel
from event_schema import Event
from location_schema import Location

class Item(BaseModel):
    id:str
    event:Event
    location:Location
    amount:int
    unit_price:float
