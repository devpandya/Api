from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .token import create_access_token
from fastapi.exceptions import HTTPException
from app.models.models import User
from sqlalchemy.orm.session import Session
from fastapi import status
from app.api_functions.hashing import Hash

def login(request:OAuth2PasswordRequestForm,db:Session):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
         raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
        
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")

    access_token = create_access_token(data={"sub":user.email})
    return {"access_token":access_token, "token_type":"bearer"}