from fastapi import APIRouter, Body
from models.user_schema import User

user_route = APIRouter()

@user_route.get("/")
def read_items():
    return [{"username": "john"}, {"username": "alice"}]

@user_route.get("/{id}")
def read_item(id: str):
    return {"El id es: ": id}

@user_route.post("/")
def create_user(user: User = Body(...)):
    try:
        return {"El usuario fue creado: ": {f"{user}"}}
    except Exception as e:
        print(e)
        return {"error:":str(e)}

@user_route.put("/{id}")
def update_user(id: int, user: User = Body(...)):
    return {"Mensaje":f"{id} fue modificado"}

@user_route.delete("/{id}")
def delete_user(id: int):
    return {"Mensaje":"{id} fue eliminado"}
