
from app.api_functions.database import get_db
from fastapi import APIRouter
from typing import List
from fastapi import status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.models import schemas
from app.logic.oauth2 import get_current_user
from app.logic import todo

router = APIRouter(prefix="/todo", tags=['ToDo'])

@router.get('/', response_model=List[schemas.ToDoResponse],)
async def get_todos(db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return todo.get_todos(db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ToDoResponse)
async def get_todo(id:int, db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return todo.get_todo(id,db)

@router.post('/',status_code=status.HTTP_201_CREATED)
async def add_todo(newTodo:schemas.ToDo,db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return todo.add_todo(newTodo,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_todo(id:int,request: schemas.ToDo,db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return todo.update_todo(id,request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id:int,db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return todo.delete_todo(id,db)
