from fastapi import APIRouter, Body
from models.item_schema import Item
from database import ItemModel

item_route = APIRouter()

    
@item_route.post("/")
def create_items(item: Item = Body(...)):
    ItemModel.create(event_id=item.event_id , location_id=item.location_id , amount=item.amount , unit_price=item.unit_price )
    return {"message": "Item created successfully"}
    
@item_route.get("/")
def get_items():
    item = ItemModel.select().where(ItemModel.id > 0).dicts()
    return list(item)

@item_route.get("/{item_id}")
def get_item(item_id: int):
    try:
        item = ItemModel.get(ItemModel.id == item_id)
        return item
    except ItemModel.DoesNotExist:
        return {"error": "Item not found"}


@item_route.put("/{item_id}")
def update_item(item_id: int, item: Item = Body(...)):
    try:
        new_item = ItemModel.get(ItemModel.id == item_id)
        new_item.event_id = item.event_id
        new_item.location_id = item.location_id
        new_item.amount = item.amount
        new_item.unit_prive = item.unit_price
        new_item.save()
        return {"Mensaje":"Item Update successfully"}
    except ItemModel.DoesNotExist:
        return {"error": "Item not found"}
    
@item_route.delete("/{item_id}")
def delete_item(item_id: int):
    rows_deleted = ItemModel.delete().where(ItemModel.id == item_id).execute()
    if rows_deleted:
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}
