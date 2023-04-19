from fastapi import FastAPI
from .routers import blocks

from .database.database import engine
from .database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blocks.router)