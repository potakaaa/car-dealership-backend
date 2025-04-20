from sqlalchemy.orm import Session
from app.schemas.user import LoginRequest, VerificationCode
from app.models.user import User
from app.utils.whatsapp.whatsapp_api import generate_and_send_code
from app.utils.redis.redisCache import redis_cache
from app.utils.redis.redisClient import redis_client
from fastapi import HTTPException

async def login_or_signup(db: Session, payload: LoginRequest):
    result = db.query(User).filter(User.phone_number == payload.phone_number).first()
    user = result

    if not user:
        print("User not found, creating new user")
        user = User(phone_number=payload.phone_number, username=payload.username)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    print("User found or created")

    code = await generate_and_send_code(payload.phone_number)

    return redis_cache(
        key=f"otp_{payload.phone_number}",
        cacheTime=300,
        result={"message": "Verification code sent successfully", "code": code},
    )

async def verify_code(db: Session, payload: VerificationCode):
    stored_code = redis_client.get(f"otp:{payload.phone_number}")
    if not stored_code:
        raise HTTPException(status_code=400, detail="Invalid or Expired Code")
    
    result = db.query(User).filter(User.phone_number == payload.phone_number).first()
    user = result

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_verified = True
    db.commit()
    db.refresh(user)
    
    return {"message": "User verified successfully"}