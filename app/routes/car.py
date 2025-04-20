from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.car import CarAdd, Car
from app.services import car
from app.utils.apiResponse import ApiResponse
from app.utils.db.getDb import get_db

router = APIRouter()

@router.get("/cars", response_model=ApiResponse)
def get_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = car.get_cars(db, skip=skip, limit=limit)
    return ApiResponse(data=cars)

@router.get("/cars/{car_id}", response_model=ApiResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = car.get_car_by_id(db, car_id=car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return ApiResponse(data=car)

@router.post("/cars", response_model=ApiResponse)
def add_car(car: CarAdd, db: Session = Depends(get_db)):
    car = car.add_car(db=db, car=car)
    return ApiResponse(data=Car.from_orm(car))

@router.put("/cars/{car_id}", response_model=ApiResponse)
def buy_car(car_id: int, db: Session = Depends(get_db)):
    car = car.mark_as_sold(db=db, car_id=car_id)
    return ApiResponse(data=Car.from_orm(car))

