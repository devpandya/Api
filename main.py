from app.routers import todo, user,auth
from fastapi import FastAPI
from app.models import models
from app.api_functions.database import  engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(todo.router)