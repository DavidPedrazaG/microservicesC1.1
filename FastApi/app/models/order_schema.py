from pydantic import BaseModel
from datetime import date;
from enum import Enum
from typing import List
import item_schema

class Estado(Enum):
    Pendente = "Pendente"
    Concluido = "Concluido"
    Cancelado = "Cancelado"
class PurchaseOrder(BaseModel):
    id:str
    order_code:str
    user_id:str
    items: List[item_schema.Item]
    total:float
    date:date
    state = Estado
    
