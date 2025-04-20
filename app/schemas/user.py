from pydantic import BaseModel

class LoginRequest(BaseModel):
    phone_number: str
    username: str

class VertificationCode(BaseModel):
    phone_number: str
    code: str