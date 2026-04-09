from fastapi import APIRouter,Depends
from ..database import get_db
from sqlalchemy.orm import Session
from app import models

router = APIRouter()

@router.get("/{short_link}")
def url_finder(short_link: str, db : Session = Depends(get_db)):
    query = db.query(models.urlsConverted).filter(models.urlsConverted.short_URL == short_link).first()
    if query:
        return {"message" : "found"}
    raise Exception