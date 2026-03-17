from .session import get_session
from .models import Post


def get_post(id : int)-> Post | None:
    with get_session() as session:
        post = session.get(Post, id)
        return post
    
def create_post(title: str, content:str, user_id: int) -> int:
    with get_session() as session:
        post = Post(title=title, content=content, user_id=user_id)
        session.add(post)
        session.flush()
        
        return post.id
    
def update_post(id: int, title: str, content:str) -> Post | None:
    with get_session() as session:
        post = session.get(Post, id)
        
        if post is None:
            return None
        
        post.title = title
        post.content = content
        
        return post
    
def delete_post(id: int):
    with get_session() as session:
        post = session.get(Post, id)
        
        if post is not None:
            session.delete(post)