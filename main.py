from fastapi import FastAPI
from app.database import engine, Base
from app.controllers.tarefa_controller import router
import app.models.tarefa_model

Base.metadata.create_all(bind=engine)

app = FastAPI() 

app.include_router(router)