from fastapi import APIRouter, Body
from models.location_schema import Location

location_route = APIRouter()

@location_route.post("/")
def create_location(location: Location = Body(...)):
    try:
        return Location
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@location_route.get("/")
def read_location():
    return [{"name": "VIP"}, {"price": "50.000"}]

@location_route.post("/")
def create_location(location: Location = Body(...)):
    try:
        return {"El usuario fue creado: ": {f"{location}"}}
    except Exception as e:
        print(e)
        return {"error:":str(e)}

@location_route.put("/{id}")
def update_location(id: int, location: Location = Body(...)):
    return {"Mensaje":f"{id} fue modificado"}

@location_route.delete("/{id}")
def delete_location(id: int):
    return {"Mensaje":"{id} fue eliminado"}

