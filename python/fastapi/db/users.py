from .connection import get_db
from .session import get_session
from .models import User

# def init():
#     with get_db() as con:
#         with con.cursor() as cur:
#             cur.execute(
#                 """
#                 create table if not exists users(
#                     id serial primary key,
#                     name text not null,
#                     age integer not null
#                 )
#                 """)


def get_user(user_id: int) -> User | None:
    with get_session() as session:
        #user = session.query(User).filter(User.id == user_id).first()
        user = session.get(User, user_id)
        return user


def create_user(name: str, age: int) -> int:
    with get_session() as session:
        user = User(name=name, age=age)
        session.add(user)
        session.flush()
        
        return user.id


def update_user(user_id: int, name: str, age: int) -> User | None:
    with get_session() as session:
        user = session.get(User, user_id)
        
        if user is None:
            return None
        
        user.name = name
        user.age = age
        
        return user
        

def delete_user(user_id: int):
    with get_session() as session:
        user = session.get(User, user_id)
        
        if user is not None:
            session.delete(user)
    