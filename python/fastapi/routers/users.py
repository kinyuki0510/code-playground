from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import db

router = APIRouter()

# Pydanticモデル（Week5でやったやつ）
class User(BaseModel):
    name: str
    age: int

# GET
@router.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    user = db.users.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return user

# POST
@router.post("/users")
async def create_user(user: User) -> dict:
    user_id = db.users.create_user(user.name, user.age)
    return {"id": user_id}

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    user = db.users.update_user(user_id, user.name, user.age)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int) -> dict:
    db.users.delete_user(user_id)
    return {"message": "User deleted"}
