import os
import logging
import asyncio
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Главная функция инициализации и запуска приложения"""
    try:
        logger.info("🚀 Starting Poker Mentor application...")
        
        # 1. Инициализация базы данных
        from app.database.database import init_db
        init_db()
        logger.info("✅ Database initialized")
        
        # 2. Инициализация AI клиента
        from app.ai.ai_client import AIClient  # ✅ ИСПРАВЛЕНО: app.ai.ai_client
        ai_client = AIClient()  # ✅ AIClient вместо AICClient
        logger.info("✅ AI client initialized")
        
        # 3. Запуск Telegram бота
        from app.bot.bot_core import start_bot
        from app.config import settings  # ✅ ИСПРАВЛЕННЫЙ ИМПОРТ

        bot_token = settings.TELEGRAM_BOT_TOKEN  # ✅ Используем settings
        
        if not bot_token:
            logger.error("❌ BOT_TOKEN not found in environment variables")
            return
        
        logger.info("✅ Starting Telegram bot...")
        await start_bot(bot_token)
        
    except Exception as e:
        logger.error(f"❌ Application failed to start: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())