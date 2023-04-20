from fastapi import FastAPI
from .routers import blocks, probes, measurements

from .database.database import engine
from .database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blocks.router)
app.include_router(probes.router)
app.include_router(measurements.router)