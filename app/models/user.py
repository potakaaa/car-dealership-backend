from app.db.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    is_verified = Column(Boolean, default=False)