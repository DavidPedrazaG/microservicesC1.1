from fastapi import APIRouter, Body
from models.order_schema import PurchaseOrder

order_route = APIRouter()

    
@order_route.get("/")
def read_orders():
    return [{"ordername": "john"}, {"ordername": "alice"}]

@order_route.get("/{id}#{order_code}")
def read_order(id: str, order_code: str):
    return {"id": id, "order_code": order_code}

@order_route.post("/")
def create_orders(order: PurchaseOrder = Body(...)):
    try:
        return {"La orden fue creada: ": {f"{order}"}}
    except Exception as e:
        print(e)
        return {"error:":str(e)}

@order_route.put("/{id}")
def update_order(id: int, order: PurchaseOrder = Body(...)):
    return {"Mensaje":f"{id} fue modificado"}

@order_route.delete("/{id}")
def delete_order(id: int):
    return {"Mensaje":"{id} fue eliminado"}
