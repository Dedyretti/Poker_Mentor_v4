import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Telegram Bot Configuration
    TELEGRAM_BOT_TOKEN: str
    BOT_TOKEN: Optional[str] = None
    
    # Database Configuration
    DATABASE_URL: str = "sqlite:///./poker_mentor.db"
    REDIS_URL: str = "redis://localhost:6379"
    
    # AI Configuration
    OPENAI_API_KEY: str
    AI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4"
    AI_TIMEOUT: int = 30
    
    # Game Configuration
    DEFAULT_STACK: int = 1000
    DEFAULT_BLIND: int = 10
    
    # Webhook Configuration
    WEBHOOK_URL: str = "https://your-domain.com"
    WEBHOOK_PATH: str = "/webhook"
    
    class Config:
        env_file = ".env"

# Создаем глобальный экземпляр настроек
settings = Settings()

# Для обратной совместимости
TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
BOT_TOKEN = settings.BOT_TOKEN or settings.TELEGRAM_BOT_TOKEN
DATABASE_URL = settings.DATABASE_URL
REDIS_URL = settings.REDIS_URL
AI_API_KEY = settings.AI_API_KEY
WEBHOOK_URL = settings.WEBHOOK_URL
WEBHOOK_PATH = settings.WEBHOOK_PATH