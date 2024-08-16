from fastapi import APIRouter, Body
from ..models.order_schema import PurchaseOrder, ItemOrder

user_route = APIRouter()

@user_route.post("/")
def create_users(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@user_route.get("/")
def read_users():
    return [{"username": "john"}, {"username": "alice"}]

@user_route.get("/{id}")
def read_user(id: int):
    return {"id": id}

@user_route.put("/{id}")
def update_user(id: int, user: User = Body(...)):
    return user