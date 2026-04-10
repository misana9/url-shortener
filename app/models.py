from .database import Base
from sqlalchemy import Column,Integer,String

class urlsConverted(Base):
    __tablename__ = "URLS"

    id = Column(Integer, primary_key=True,nullable=False)
    long_URL = Column(String,nullable=False)
    short_URL = Column(String,nullable=False)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False, unique=True)
    password = Column(String,nullable=False)