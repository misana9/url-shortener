from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from ..database import get_db
from ..utils import hash_password
from app import models

router = APIRouter()

@router.post("/register")
def create_user(user: schemas.user, db: Session=Depends(get_db)):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()