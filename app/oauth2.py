from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from app.config import settings
from app import schemas
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db

from jwt.exceptions import InvalidTokenError

from fastapi import Depends, HTTPException,status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str,credential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

        id : Optional[str] = payload.get("user_id")
        if id is None:
            print("hello")

        token_data = schemas.tokenData(id=id)# type: ignore
    except InvalidTokenError:           
        raise credential_exception
    
    return token_data

    
def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail="Could not validate credentials", 
                                        headers={"WWW-Authenticate":"Bearer"})
    
    return verify_access_token(token,credentials_exception)