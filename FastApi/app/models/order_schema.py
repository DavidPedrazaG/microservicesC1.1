from pydantic import BaseModel
from datetime import date
from enum import Enum

class Estado(Enum):
    Pendente = "Pendente"
    Concluido = "Concluido"
    Cancelado = "Cancelado"

class PurchaseOrder(BaseModel):
    id: int
    order_code: str
    user_id: str
    total: float
    date: date
    state: Estado = Estado.Pendente