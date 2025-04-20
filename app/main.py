from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import car
from app.routes import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

prefix = "/api/v1"

app.include_router(car.router, tags=["cars"], prefix=prefix)
app.include_router(user.router, tags=["users"], prefix=prefix)