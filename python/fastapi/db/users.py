from db.connection import get_db

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


def get_user(user_id: int):
    with get_db() as con:
        with con.cursor() as cur:
            cur.execute(
                """
                select id, name, age from users where id = %s
                """, (user_id,))
            user = cur.fetchone()

    if user is None:
        return None

    return {"id": user[0], "name": user[1], "age": user[2]}


def create_user(name: str, age: int) -> int:
    with get_db() as con:
        with con.cursor() as cur:
            cur.execute(
                """
                insert into users (name, age) values (%s, %s) returning id
                """, (name, age))
            user_id = cur.fetchone()[0]

    return user_id


def update_user(user_id: int, name: str, age: int) -> dict | None:
    with get_db() as con:
        with con.cursor() as cur:
            cur.execute(
                """
                update users set name = %s, age = %s where id = %s
                returning id, name, age
                """, (name, age, user_id))
            user = cur.fetchone()

    return {"id": user[0], "name": user[1], "age": user[2]} if user else None


def delete_user(user_id: int):
    with get_db() as con:
        with con.cursor() as cur:
            cur.execute(
                """
                delete from users where id = %s
                """, (user_id,))
