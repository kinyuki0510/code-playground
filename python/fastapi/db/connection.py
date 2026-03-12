import os
import psycopg2
import psycopg2.pool
from contextlib import contextmanager

def get_connect():
    return psycopg2.connect(os.environ["DATABASE_URL"])

# after: プールから取得・返却
pool = psycopg2.pool.SimpleConnectionPool(1, 10, dsn=os.environ["DATABASE_URL"])

@contextmanager
def get_db():
    con = pool.getconn()   # プールから借りる
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        pool.putconn(con)  # closeせず返却
