from fastapi import APIRouter, Body
from models.user_schema import User
from database import UserModel

user_route = APIRouter()

@user_route.post("/")
def create_users(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password = user.password)
    return {"message": "User created successfully"}
    
@user_route.get("/")
def get_users():
    user = UserModel.select().where(UserModel.id > 0).dicts()
    return list(user)

@user_route.get("/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        return {"error": "User not found"}