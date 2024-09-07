from fastapi import APIRouter, Body
from models.order_schema import PurchaseOrder
from database import OrderModel

order_route = APIRouter()

    
@order_route.post("/")
def create_orders(order: PurchaseOrder = Body(...)):
    OrderModel.create(order_code=order.order_code, user_id=order.user_id, total = order.total, order_date = order.date, state = order.state)
    return {"message": "Order created successfully"}
    
@order_route.get("/")
def get_orders():
    order = OrderModel.select().where(OrderModel.id > 0).dicts()
    return list(order)

@order_route.get("/{order_id}")
def get_order_by_id(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        return order
    except OrderModel.DoesNotExist:
        return {"error": "Order not found"} 

@order_route.put("/{order_id}")
def update_order(order_id: int, order: PurchaseOrder = Body(...)):
    try:
        new_order = OrderModel.get(OrderModel.id == order_id)
        new_order.user_id = order.user_id
        new_order.total = order.total
        new_order.order_date = order.date
        new_order.state = order.state
        new_order.save()
        return {"Mensaje":"Order Update successfully"}
    except OrderModel.DoesNotExist:
        return {"error": "Order not found"}
    
@order_route.delete("/")
def delete_order_by_id(order_id: int):
    rows_deleted = OrderModel.delete().where(OrderModel.id == order_id).execute()
    if rows_deleted:
        return {"message": "Order deleted successfully"}
    else:
        return {"error": "Order not found"}