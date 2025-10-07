import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Telegram Bot
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")
    WEBHOOK_PATH: str = "/webhook"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./poker_mentor.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # AI API
    AI_API_URL: str = os.getenv("AI_API_URL", "")
    AI_API_KEY: str = os.getenv("AI_API_KEY", "")

settings = Settings()