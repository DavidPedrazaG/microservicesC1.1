from pydantic import BaseModel
from datetime import date;
from enum import Enum
from typing import List
from item_schema import Item

class Estado(Enum):
    Pendente = "Pendente"
    Concluido = "Concluido"
    Cancelado = "Cancelado"
class PurchaseOrder(BaseModel):
    id:str
    order_code:str
    user_id:str
    items: List[Item]
    total:float
    date:date
    state = Estado
    
