from fastapi import APIRouter, Body
from ..models.event_schema import Event

event_route = APIRouter()

@event_route.post("/")
def create_events(event: Event = Body(...)):
    try:
        return Event
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@event_route.get("/")
def read_events():
    return [{"name": "Aventura"}, {"address": "10 street, Bolivar Avenue"}]

@event_route.get("/{id}")
def read_event(id: int):
    return {"id": id}

@event_route.put("/{id}")
def update_event(id: int, event: Event = Body(...)):
    return event

@event_route.delete("/{id}")
def delete_event(id: int):
    return {"Mensaje": "Eliminado"}
