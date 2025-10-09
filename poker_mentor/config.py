import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Telegram Bot Configuration
    TELEGRAM_BOT_TOKEN: str
    
    # Database Configuration
    DATABASE_URL: str = "sqlite:///./poker_mentor.db"
    REDIS_URL: str = "redis://localhost:6379"
    
    # AI Configuration
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4"
    AI_TIMEOUT: int = 30
    
    # Game Configuration
    DEFAULT_STACK: int = 1000
    DEFAULT_BLIND: int = 10
    
    class Config:
        env_file = ".env"

# Создаем глобальный экземпляр настроек
settings = Settings()