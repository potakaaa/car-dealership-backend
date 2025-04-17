from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.carSchema import CarAdd, Car
from app.services import carService
from app.db.database import SessionLocal
from app.utils.apiResponse import ApiResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cars", response_model=ApiResponse)
def get_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = carService.get_cars(db, skip=skip, limit=limit)
    return ApiResponse(data=cars)

@router.get("/cars/{car_id}", response_model=ApiResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = carService.get_car_by_id(db, car_id=car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return ApiResponse(data=car)

@router.post("/cars", response_model=ApiResponse)
def add_car(car: CarAdd, db: Session = Depends(get_db)):
    car = carService.add_car(db=db, car=car)
    return ApiResponse(data=Car.from_orm(car))

@router.put("/cars/{car_id}", response_model=ApiResponse)
def buy_car(car_id: int, db: Session = Depends(get_db)):
    car = carService.mark_as_sold(db=db, car_id=car_id)
    return ApiResponse(data=Car.from_orm(car))

