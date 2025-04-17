from sqlalchemy.orm import Session
from app.models.carModel import Car
from app.schemas.carSchema import CarAdd
from app.schemas.carSchema import Car as CarResponse
from fastapi import HTTPException
from app.utils.redis.redisClient import redis_client
from app.utils.redis.redisCache import redis_cache
import json

def get_cars(db: Session, skip: int = 0, limit: int = 10):

    cars = db.query(Car).offset(skip).limit(limit).all()
    data = [CarResponse.from_orm(car) for car in cars]

    return redis_cache(
        key=f"cars_{skip}_{limit}",
        cacheTime=300,
        result=data,
    )

def get_car_by_id(db: Session, car_id: int):

    car = db.query(Car).filter(Car.id == car_id).first()
    data = CarResponse.from_orm(car)

    return redis_cache(
        key=f"car_{car_id}",
        cacheTime=300,
        result=data,
    )

def add_car(db: Session, car: CarAdd):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def mark_as_sold(db: Session, car_id: int):
    car = db.query(Car).filter(Car.id == car_id).first()
    
    if car.is_sold:
        raise HTTPException(status_code=400, detail="Car already sold")
    
    if car:
        car.is_sold = True
        db.commit()
        db.refresh(car)
    return car