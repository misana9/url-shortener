from pydantic import BaseModel, HttpUrl
from typing import Optional

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