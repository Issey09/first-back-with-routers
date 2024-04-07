from fastapi import FastAPI


from src.database import engine, Base, SessionLocal
from src.routers import router1

app = FastAPI()
Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(router1)