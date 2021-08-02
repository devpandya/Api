
from app.api_functions.database import get_db
from fastapi import APIRouter
from typing import List
from fastapi import status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.models import schemas
from app.logic.oauth2 import get_current_user
from app.logic import user

router = APIRouter(prefix="/user", tags=['User'])

@router.post('/',status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create_user(request,db)


@router.get('/',tags=['User'],response_model=List[schemas.UserResponse])
async def get_users(db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.get_users(db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
async def get_user(id:int, db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.get_user(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_user(id:int,request: schemas.User,db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.update_user(id,request,db)

