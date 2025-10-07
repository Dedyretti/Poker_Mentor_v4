from app.bot.bot_core import bot
from app.config import settings
from app.utils.logger import setup_logger


# Импортируем обработчики чтобы они зарегистрировались
from app.bot.handlers import start, quick_game, profile
\
#from aiogram import Bot, Dispatcher
#from aiogram.client.default import DefaultBotProperties
#from aiogram.enums import ParseMode


setup_logger()


def main():
    """Главная функция запуска приложения"""
    if settings.WEBHOOK_URL:
        # Режим вебхука (для продакшена)
        from app.bot.bot_core import setup_webhook
        setup_webhook()
        print("🤖 Webhook mode - bot is ready")
    else:
        # Режим поллинга (для разработки)
        print("🤖 Бот запускается в режиме поллинга...")
        print("✅ Poker Mentor Bot готов к работе!")
        print("📱 Перейди в Telegram и напиши /start")
        bot.infinity_polling()



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
    '''
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
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot stopped with error: {e}")
    finally:
        await bot.session.close() временная заглушка'''
        
    print("Initializing Poker Mentor...")
    
    # Инициализация базы данных
    init_db()
    print("Database initialized successfully!")
    
    # Здесь позже добавим инициализацию бота и AI
    print(f"Configuration loaded: DEBUG={config.DEBUG}")


if __name__ == "__main__":
    main()