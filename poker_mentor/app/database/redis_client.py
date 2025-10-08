import redis
from Poker_Mentor_v4.poker_mentor.config import config

# Создаем подключение к Redis
redis_client = redis.Redis.from_url(config.REDIS_URL, decode_responses=True)

def get_redis():
    """Получение клиента Redis"""
    return redis_client

def set_session_data(session_id: str, data: dict, expire: int = 3600):
    """Сохранение данных сессии в Redis"""
    redis_client.setex(f"session:{session_id}", expire, str(data))

def get_session_data(session_id: str):
    """Получение данных сессии из Redis"""
    data = redis_client.get(f"session:{session_id}")
    return eval(data) if data else None

def delete_session_data(session_id: str):
    """Удаление данных сессии из Redis"""
    redis_client.delete(f"session:{session_id}")