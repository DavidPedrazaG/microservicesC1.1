from pydantic import BaseModel
from datetime import date;
from enum import Enum
from typing import List
from event_schema import Event
from location_schema import Location

class Estado(Enum):
    Pendente = "Pendente"
    Concluido = "Concluido"
    Cancelado = "Cancelado"

class ItemOrder:
    id:str
    event:Event
    location:Location
    amount:int
    unit_price:float

class PurchaseOrder(BaseModel):
    id:str
    order_id:str
    user_id:str
    items: List[ItemOrder]
    total:float
    date:date
    state = Estado
    
