from fastapi import APIRouter, Depends
from app import schemas
from .. import database
from sqlalchemy.orm import Session
from app import utils,models


router = APIRouter(
    prefix = "/url"
)

@router.post("/")
def url_shortener(url : schemas.urlFormat, db: Session = Depends(database.get_db), short_link = utils.generate_short_code()):
    query = db.query(models.urlsConverted).filter(models.urlsConverted.long_URL == url.long_URL).first()
    if query:
        return query.long_URL
    new_link = models.urlsConverted(short_URL = short_link, **url.model_dump())
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return {"message": "done"}
