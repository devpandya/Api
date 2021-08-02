from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.models import schemas,models

def get_todos(db: Session):
    todos = db.query(models.ToDo).all();
    return todos

def get_todo(id:int, db: Session):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id).first();
    if not todo:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="ToDo Not Found")
    return todo
def add_todo(todo:schemas.ToDo,db: Session):
    new_todo = models.ToDo(activity= todo.activity, owner_id = 1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(id:int,request: schemas.ToDo,db: Session):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id)
    if not todo.first():
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="ToDo Not Found")
    todo.update(request);
    db.commit()
    return 'updated'

def delete_todo(id:int,db: Session):
    todo = db.query(models.ToDo).filter(models.ToDo.id == id)
    if not todo.first():
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="ToDo Not Found")
    todo.delete(synchronize_session=False);
    db.commit()
    return 'Done'
