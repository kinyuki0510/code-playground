from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import db

router = APIRouter()

class Post(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    

@router.get("/posts/{id}")
async def get_post(id: int) -> Post:
    post = db.posts.get_post(id)
    
    if post is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return Post(id=post.id, title=post.title, content=post.content, user_id=post.user_id)

@router.post("/posts")
async def create_post(post: Post)-> dict:
    id = db.posts.create_post(post.title, post.content, post.user_id)
    return {"id": id}

@router.put("/posts/{id}")
async def update_post(id: int, post:Post) ->Post:
    post = db.posts.update_post(id, post.title, post.content)
    
    if post is None:
        raise HTTPException(status_code=404, detail="Not Found")
        
    return post

@router.delete("/posts/{id}")
async def delete_post(id: int) -> dict:
    db.posts.delete_post(id)
    return {"message": "Post deleted"}