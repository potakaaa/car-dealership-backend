from schemas.user import LoginRequest, VerificationCode
from sqlalchemy.orm import Session
from models.user import User
from utils.whatsapp.whatsapp_api import generate_and_send_code
from utils.redis.redisCache import redis_cache
from utils.redis.redisClient import redis_client
from fastapi import HTTPException

async def login_or_signup(db: Session, payload: LoginRequest):
    result = await db.query(User).filter(User.phone_number == payload.phone_number).first()
    user = result.scalar_one_or_none()

    if not user:
        user = User(phone_number=payload.phone_number, username=payload.username)
        db.add(user)
        db.commit()
        db.refresh(user)

    code = await generate_and_send_code(payload.phone_number)

    return redis_cache(
        key=f"otp_{payload.phone_number}",
        cacheTime=300,
        result={"message": "Verification code sent successfully", "code": code},
    )

async def verify_code(db: Session, payload: VerificationCode):
    stored_code = await redis_client.get(f"otp:{payload.phone_number}")
    if not stored_code:
        raise HTTPException(status_code=400, detail="Invalid or Expired Code")
    
    result = await db.query(User).filter(User.phone_number == payload.phone_number).first()
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_verified = True
    db.commit()
    db.refresh(user)
    
    return {"message": "User verified successfully"}