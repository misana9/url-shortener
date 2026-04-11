from fastapi import APIRouter, Depends,HTTPException,status
from app import schemas
from .. import database
from sqlalchemy.orm import Session
from app import utils,models
from ..oauth2 import get_current_user

router = APIRouter(
    prefix = "/url"
)

@router.post("/")
def url_shortener(url : schemas.urlFormat, db: Session = Depends(database.get_db), current_user:str = Depends(get_current_user)):
    short_link = utils.generate_short_code()
    query = db.query(models.urlsConverted).filter(models.urlsConverted.long_URL == str(url.long_URL) ).first()
    if query:
        return query.long_URL
    new_link = models.urlsConverted(short_URL = short_link, **url.model_dump(mode="json"))
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return {"message": "done"}
