from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import schemas
from ..database import get_db
from ..utils import hash_password
from app import models

router = APIRouter()

@router.post("/register")
def create_user(user: schemas.user, db: Session=Depends(get_db)):
    existing_user_query = db.query(models.Users).filter(user.email == models.Users.email).first() #type: ignore
    if existing_user_query:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already registered")
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()