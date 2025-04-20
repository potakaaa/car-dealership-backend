from pydantic import BaseModel

class LoginRequest(BaseModel):
    phone_number: str
    username: str

class VerificationCode(BaseModel):
    phone_number: str
    username: str
    code: str