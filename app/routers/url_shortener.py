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
    new_link = models.urlsConverted(short_URL = short_link, **url.model_dump())
    db.add(new_link)
    db.commit()
    return {"message": "done"}