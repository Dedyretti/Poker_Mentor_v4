import os
import logging
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
        logger.info("Starting Poker Mentor application...")
        
        # 1. Инициализация базы данных (Участник B)
        from app.database.database import init_db
        init_db()
        logger.info("✅ Database initialized")
        
        # 2. Инициализация AI (Участник C)
        from app.ai.ai_client import AIClient
        ai_client = AIClient()
        logger.info("✅ AI client initialized")
        
        # 3. Запуск Telegram бота (Участник A)
        from app.bot.bot_core import start_bot
        bot_token = os.getenv("BOT_TOKEN")
        
        if not bot_token:
            logger.error("❌ BOT_TOKEN not found in environment variables")
            return
        
        logger.info("✅ Starting Telegram bot...")
        await start_bot(bot_token)
        
    except Exception as e:
        logger.error(f"❌ Application failed to start: {e}")
        raise

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())