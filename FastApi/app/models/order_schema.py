from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import List
from models import item_schema

class Estado(Enum):
    Pendente = "Pendente"
    Concluido = "Concluido"
    Cancelado = "Cancelado"

class PurchaseOrder(BaseModel):
    id: int
    order_code: str
    user_id: str
    items: List[item_schema.Item]
    total: float
    date: date
    state: Estado = Estado.Pendente