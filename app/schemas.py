from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class urlFormat(BaseModel):
    long_URL : HttpUrl

class user(BaseModel):
    email : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class tokenData(BaseModel):
    id : Optional[int] = None

class urlOut(BaseModel):
    long_URL : str
    short_URL: str
    created_at : datetime

    class Config:
        from_attributes = True
