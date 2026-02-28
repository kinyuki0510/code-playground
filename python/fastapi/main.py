# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydanticモデル（Week5でやったやつ）
class User(BaseModel):
    name: str
    age: int

# インメモリDB（簡易）
users: dict[int, User] = {}
counter = 0

# GET
@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    return users[user_id]

# POST
@app.post("/users")
async def create_user(user: User) -> dict:
    global counter
    counter += 1
    users[counter] = user
    return {"id": counter}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    users[user_id] = user
    return users[user_id]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    users.pop(user_id)
    return {"message": "削除しました"}