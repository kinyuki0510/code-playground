# main.py

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from routers import users
import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("アプリケーションの起動前の処理")
    yield
    print("アプリケーションの終了前の処理")

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
