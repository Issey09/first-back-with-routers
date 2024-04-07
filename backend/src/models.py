from sqlalchemy import Column, String, Integer, TIMESTAMP

from src.database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    nickname = Column(String, index=True)