import asyncio
import logging
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.bot_core import setup_bot
from app.config import settings , config
from app.database.database import init_db
from app.utils.logger import setup_logging


logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app=None):
    """Управление жизненным циклом приложения"""
    # Инициализация базы данных
    await init_db()
    logger.info("Application started")
    yield
    logger.info("Application shutdown")

async def main():
    """Главная функция приложения"""
    setup_logging()
    init_db()
    # Инициализация бота
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Настройка бота
    await setup_bot(bot, dp)
    
    # Запуск бота
    logger.info("Starting bot...")
    ry:t
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot stopped with error: {e}")
    finally:
        await bot.session.close()
        
    print("Initializing Poker Mentor...")
    
    print("Database initialized successfully!")
    
    # Здесь позже добавим инициализацию бота и AI
    print(f"Configuration loaded: DEBUG={config.DEBUG}")

if __name__ == "__main__":
    main()
