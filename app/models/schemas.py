from typing import List, Optional
from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password:str

class ToDo(BaseModel):
    activity:str
    class Config():
        orm_mode=True

class User(BaseModel):
    name: str
    email: str
    password:str

class UserResponse(BaseModel):
    name: str
    email: str
    todos: List[ToDo]
    class Config():
        orm_mode=True


class ToDoResponse(ToDo):
    activity:str
    owner:UserResponse
    class Config():
        orm_mode=True


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None
