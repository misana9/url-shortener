from fastapi import APIRouter, Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from app import models
from ..utils import verify_password
from app import oauth2

router = APIRouter()

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if not verify_password(user_credentials.password,user.password):# type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id" : user.id}) # type: ignore

    return {"access_token" : access_token, "token_type" : "bearer"} 