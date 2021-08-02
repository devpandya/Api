
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from .token import verify_token

outh2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user (token:str= Depends(outh2_scheme)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenicate":"Bearer"})

    return verify_token(token,credentials_exception)
