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
        logger.info("🚀 Starting Poker Mentor PRODUCTION...")
        
        # 1. Инициализация базы данных
        from app.database.database import init_db
        init_db()
        logger.info("✅ Database initialized")
        
        # 2. Инициализация AI клиента
        from app.ai.ai_client import AIClient
        ai_client = AIClient()
        logger.info("✅ AI client initialized")
        
        # 3. Запуск Telegram бота в режиме POLLING
        from app.bot.bot_core import start_bot
        from app.config import settings

        bot_token = settings.TELEGRAM_BOT_TOKEN
        
        if not bot_token:
            logger.error("❌ BOT_TOKEN not found in environment variables")
            return
        
        logger.info("✅ Starting Telegram bot in POLLING mode...")
        
        # Запускаем бота (блокирующий вызов)
        await start_bot(bot_token)
        
    except Exception as e:
        logger.error(f"❌ Application failed to start: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())