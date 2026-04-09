from .database import Base
from sqlalchemy import Column,Integer,String

class urlsConverted(Base):
    __tablename__ = "URLS"

    id = Column(Integer, primary_key=True,nullable=False)
    long_URL = Column(String,nullable=False)
    short_URL = Column(String,nullable=False)