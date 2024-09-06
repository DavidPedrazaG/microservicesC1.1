from pydantic import BaseModel

class Event(BaseModel):
    id : str
    name : str 
    address : str
    city : str
    description : str
    
