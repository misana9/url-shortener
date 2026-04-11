from fastapi import APIRouter, Depends,HTTPException,status
from app import schemas
from .. import database
from sqlalchemy.orm import Session
from app import utils,models
from ..oauth2 import get_current_user
from typing import List

router = APIRouter(
    prefix = "/url"
)

@router.post("/")
def url_shortener(url : schemas.urlFormat, db: Session = Depends(database.get_db), current_user:str = Depends(get_current_user)):
    short_link = utils.generate_short_code()
    query = db.query(models.urlsConverted).filter(models.urlsConverted.long_URL == str(url.long_URL) ).first()
    if query:
        return query.long_URL
    new_link = models.urlsConverted(short_URL = short_link, **url.model_dump(mode="json"), owner_id = current_user.id) #type: ignore
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return {"message": "done"}


@router.delete("/{id}")
def url_delete(id:int, db : Session = Depends(database.get_db), current_user:str = Depends(get_current_user)):
    query = db.query(models.urlsConverted).filter(models.urlsConverted.id == id)
    post = query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No post found")
    if post.owner_id != current_user.id: #type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    query.delete(synchronize_session=False)
    db.commit()
        
@router.get("/user-links",response_model=List[schemas.urlOut])
def get_url(db : Session = Depends(database.get_db), current_user : str = Depends(get_current_user)):
    query = db.query(models.urlsConverted).filter(models.urlsConverted.owner_id == current_user.id).all() #type: ignore
    return query