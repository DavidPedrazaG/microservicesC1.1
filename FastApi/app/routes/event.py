from fastapi import APIRouter, Body
from models.event_schema import Event
from database import EventModel

event_route = APIRouter()

@event_route.post("/")
def create_events(event: Event = Body(...)):
    EventModel.create(Eventname=event.Eventname, email=event.email, city = event.city)
    return {"message": "Event created successfully"}
    
@event_route.get("/")
def get_events():
    event = EventModel.select().where(EventModel.id > 0).dicts()
    return list(event)

@event_route.get("/{event_id}")
def get_event(event_id: int):
    try:
        event = EventModel.get(EventModel.id == event_id)
        return event
    except EventModel.DoesNotExist:
        return {"error": "Event not found"}
    

@event_route.put("/{event_id}")
def update_event(event_id: int, event: Event = Body(...)):
    try:
        new_event = EventModel.get(EventModel.id == event_id)
        new_event.name = event.name
        new_event.address= event.address
        new_event.city = event.city
        new_event.description = event.description
        new_event.save()
        return {"Mensaje":"Event Update successfully"}
    except EventModel.DoesNotExist:
        return {"error": "Event not found"}
    
@event_route.delete("/{event_id}")
def delete_event(event_id: int):
    rows_deleted = EventModel.delete().where(EventModel.id == event_id).execute()
    if rows_deleted:
        return {"message": "Event deleted successfully"}
    else:
        return {"error": "Event not found"}
    