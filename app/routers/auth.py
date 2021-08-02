from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.api_functions.database import get_db
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from fastapi import APIRouter
from app.logic import auth

router = APIRouter(prefix="/auth", tags=['Auth'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(),db:Session=Depends(get_db)):
    return auth.login(request,db)