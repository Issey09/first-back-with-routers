from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session




from typing import Annotated

from src import crud
from src.database import engine, Base, SessionLocal
from src.http_client import AsyncHttpClient

from src.schemas import User






router1 = APIRouter(
    prefix='/user'
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


cmd_client = AsyncHttpClient(main_url="http://127.0.0.1:8000")


@router1.get('/get_cheese/')
async def get_cheese():
    return await cmd_client.create_user()