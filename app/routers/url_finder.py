from fastapi import APIRouter,Depends,HTTPException,status
from ..database import get_db
from sqlalchemy.orm import Session
from app import models
from fastapi.responses import RedirectResponse
from .auth import login
from app.oauth2 import get_current_user

router = APIRouter()

@router.get("/{short_link}")
def url_finder(short_link: str, db : Session = Depends(get_db)): 
    query = db.query(models.urlsConverted).filter(models.urlsConverted.short_URL == short_link).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="URL not found")
    return query.long_URL  # type: ignore