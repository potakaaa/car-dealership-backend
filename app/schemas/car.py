from pydantic import BaseModel

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float
    mileage: int
    color: str

class CarAdd(CarBase):
    pass

class Car(CarBase):
    id: int
    is_sold: bool = False

    class Config:
        from_attributes = True

