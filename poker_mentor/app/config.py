import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Настройки приложения"""
    
    # Bot
    BOT_TOKEN: str
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./poker_mentor.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Webhook (для продакшена)
    WEBHOOK_URL: Optional[str] = None
    WEBHOOK_PATH: str = "/webhook"
    
    # AI
    AI_API_URL: Optional[str] = None
    AI_API_KEY: Optional[str] = None
    
    # Game
    DEFAULT_STACK: int = 1000
    DEFAULT_BLIND: int = 10
    
    class Config:
        env_file = ".env"

settings = Settings()