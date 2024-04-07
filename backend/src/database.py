from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker



SQLALCHEMY_DATABASE_URL = "sqlite:///./ap.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()