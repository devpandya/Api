
from app.api_functions.hashing import Hash
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.models import schemas,models

def create_user(request: schemas.User,db: Session):
    new_user = models.User(name= request.name, email = request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    users = db.query(models.User).all();
    return users

def get_user(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first();
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="User Not Found")
    return user

def update_user(id:int,request: schemas.User,db: Session):
    todo = db.query(models.User).filter(models.User.id == id)
    if not todo.first():
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="User Not Found")
    todo.update(request);
    db.commit()
    return 'updated'

