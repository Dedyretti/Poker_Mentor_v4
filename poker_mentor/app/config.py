import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Настройки приложения"""
    env_file = ".env"
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

class Config(BaseSettings):
    # База данных
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/poker_mentor")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Telegram Bot
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    
    # AI API
    AI_API_KEY: str = os.getenv("AI_API_KEY", "")
    AI_API_URL: str = os.getenv("AI_API_URL", "")
    
    # Настройки приложения
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
        
settings = Settings()
config = Config()
load_dotenv()

