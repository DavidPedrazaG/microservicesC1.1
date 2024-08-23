from fastapi import APIRouter, Body
from ..models.item_schema import Item

item_route = APIRouter()

    
@item_route.get("/")
def read_items():
    return [{"itemname": "john"}, {"itemname": "alice"}]

@item_route.get("/{id}")
def read_item(id: str):
    return {"id": id}

@item_route.post("/")
def create_items(item: Item = Body(...)):
    try:
        return item
    except Exception as e:
        print(e)
        return {"error:":str(e)}

@item_route.put("/{id}")
def update_item(id: int, item: Item = Body(...)):
    return item

@item_route.delete("/{id}")
def delete_item(id: int):
    return {"Mensaje":"Eliminado"}
