from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    mileage = Column(Integer)
    color = Column(String)
    is_sold = Column(Boolean, default=False)