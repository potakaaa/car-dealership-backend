from schemas.user import LoginRequest, VertificationCode
from fastapi import APIRouter, Depends, HTTPException
from utils.apiResponse import ApiResponse
from utils.db.getDb import get_db
from models.user import User
from utils.whatsapp.whatsapp_api import generate_and_send_code

import redis.asyncio as redis
from sqlalchemy.future import select

@app.post("/login_or_signup", response_model=ApiResponse)
async def login_or_signup(payload: LoginRequest, db=Depends(get_db)):
    result = await db.execute(select(User).where(User.phone_number == payload.phone_number))
    user = result.scalar_one_or_none()

    if not user:
        user = User(phone_number=payload.phone_number, username=payload.username)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    await generate_and_send_code(payload.phone_number)
    return ApiResponse(data={"message": "Verification code sent successfully"})

