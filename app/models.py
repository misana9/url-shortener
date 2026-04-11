from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class urlsConverted(Base):
    __tablename__ = "URLS"

    id = Column(Integer, primary_key=True,nullable=False)
    long_URL = Column(String,nullable=False)
    short_URL = Column(String,nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False, unique=True)
    password = Column(String,nullable=False)