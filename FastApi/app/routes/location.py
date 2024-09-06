from fastapi import APIRouter, Body
from models.location_schema import Location
from database import LocationModel

location_route = APIRouter()

@location_route.post("/")
def create_location(location: Location = Body(...)):
    LocationModel.create(name=location.name , price=location.price, max_capacity=location.max_capacity, available_seats=location.available_seats )
    return {"message": "Location created successfully"}
    
  
@location_route.get("/")
def get_locations():
    location = LocationModel.select().where(LocationModel.id > 0).dicts()
    return list(location)

@location_route.get("/{location_id}")
def get_location(location_id: int):
    try:
        location = LocationModel.get(LocationModel.id == location_id)
        return location
    except LocationModel.DoesNotExist:
        return {"error": "Location not found"}
    

@location_route.put("/{location_id}")
def update_location(location_id: int, location: Location = Body(...)):
    try:
        new_location = LocationModel.get(LocationModel.id == location_id)
        new_location.name = location.name
        new_location.price= location.price
        new_location.max_capacity = location.max_capacity
        new_location.available_seats = location.available_seats
        new_location.save()
        return {"Mensaje":"Location Update successfully"}
    except LocationModel.DoesNotExist:
        return {"error": "Location not found"}
    
@location_route.delete("/{location_id}")
def delete_location(location_id: int):
    rows_deleted = LocationModel.delete().where(LocationModel.id == location_id).execute()
    if rows_deleted:
        return {"message": "Location deleted successfully"}
    else:
        return {"error": "Location not found"}
    