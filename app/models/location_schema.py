from pydantic import BaseModel

class Location(BaseModel):
    id : str 
    name : str 
    price : float
    max_capacity : int
    available_seats : str
    