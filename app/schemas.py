from pydantic import BaseModel, HttpUrl, computed_field
from typing import Optional
from datetime import datetime
from .config import settings

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
    id: int
    long_URL : str
    short_URL: str
    created_at : datetime

    @computed_field
    @property
    def formatted_short_url(self) -> str:
        return f"{settings.base_url}/{self.short_URL}"

    class Config:
        from_attributes = True
