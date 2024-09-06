from pydantic import BaseModel

class Location(BaseModel):
    id : int 
    name : str 
    price : float
    max_capacity : int
    available_seats : bool
    