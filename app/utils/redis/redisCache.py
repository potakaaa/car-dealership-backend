from typing import Callable, Any
import json
from app.utils.redis.redisClient import redis_client

def redis_cache(key: str, result = Any, cacheTime: int = 300, response_model = None):
    cached = redis_client.get(key)

    if cached:
        data = json.loads(cached)
        return data if response_model is None else response_model(**data) if isinstance(data, dict) else [response_model(**item) for item in data]
    
    if response_model:
        serialized = [item.dict() for item in result] if isinstance(result, list) else result.dict()
        redis_client.setex(key, cacheTime, json.dumps(serialized))
    else:
        redis_client.setex(key, cacheTime, json.dumps(result))
        return result