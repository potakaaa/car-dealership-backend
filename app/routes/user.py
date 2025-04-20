from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import LoginRequest, VerificationCode
from app.utils.apiResponse import ApiResponse
from app.utils.db.getDb import get_db
from app.models.user import User
from app.utils.whatsapp.whatsapp_api import generate_and_send_code
from app.services.user import login_or_signup, verify_code
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login_or_signup", response_model=ApiResponse)
async def authenticate(payload: LoginRequest, db: Session = Depends(get_db)):
    user = await login_or_signup(db=db, payload=payload)
    return ApiResponse(data=user)

@router.post("/verify_code", response_model=ApiResponse)
async def verify(payload: VerificationCode, db: Session = Depends(get_db)):
    user = await verify_code(db=db, payload=payload)
    return ApiResponse(data=user)
                      
                      

