import os, httpx, random
from datetime import timedelta
from fastapi import FastAPI, HTTPException
from app.utils.redis.redisClient import redis_client

async def send_message(phone_number: str, code: str):
    payload = {
        "messaging_product": "whatsapp",
        "to": {phone_number},
        "type": "template",
        "template": {
            "name": "verify_code",
            "language": {
                "code": "en_US"
                },
            "components": [
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [
                        {
                            "type": "text",
                            "text": {code}  
                        }
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "copy_code",
                    "index": "1"
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": {code}
                        }
                        ]
                    }
                ]
            }
        }
    headers = {"Authorization" : f"Bearer {os.getenv('WHATSAPP_API_TOKEN')}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(os.getenv('WHATSAPP_API_URL'), json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to send verification code")
        
async def generate_and_send_code(phone_number: str):
    code = str(random.randint(100000, 999999))
    await redis_client.setex(f"otp:{phone_number}", timedelta(minutes=5), code)
    await send_message(phone_number, code)

    return code
    