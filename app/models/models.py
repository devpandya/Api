from sqlalchemy.sql.schema import ForeignKey
from app.api_functions.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

class ToDo(Base):
    __tablename__="ToDo"
    id = Column(Integer,primary_key=True,index=True)
    activity= Column(String)
    owner_id = Column(Integer,ForeignKey('User.id'))

    owner = relationship("User",back_populates="todos")

class User(Base):
    __tablename__="User"
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String)
    email= Column(String)
    password= Column(String)

    todos =relationship("ToDo",back_populates="owner")