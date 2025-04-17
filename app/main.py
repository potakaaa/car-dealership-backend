from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import carRoute

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(carRoute.router, tags=["cars"], prefix="/api/v1")