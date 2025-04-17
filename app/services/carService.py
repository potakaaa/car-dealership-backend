from sqlalchemy.orm import Session
from app.models.carModel import Car
from app.schemas.carSchema import CarAdd
from fastapi import HTTPException

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).offset(skip).limit(limit).all()

def get_car_by_id(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

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