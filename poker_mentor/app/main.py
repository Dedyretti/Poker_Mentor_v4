from app.bot.bot_core import bot
from app.config import settings
from app.utils.logger import setup_logger

# Импортируем все обработчики чтобы они зарегистрировались
from app.bot.handlers import start, profile, quick_game

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

if __name__ == "__main__":
    main()