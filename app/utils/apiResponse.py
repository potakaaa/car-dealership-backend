from pydantic import BaseModel
from typing import Any

class ApiResponse(BaseModel):
    status: str = "success"
    data: Any

    class Config:
        from_attributes = True