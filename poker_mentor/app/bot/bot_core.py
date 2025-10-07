import logging
import telebot
from app.config import settings

# Инициализация бота
bot = telebot.TeleBot(settings.BOT_TOKEN)

# Настройка логирования
logger = logging.getLogger(__name__)

def setup_webhook():
    """Настройка вебхука для продакшена"""
    webhook_url = f"{settings.WEBHOOK_URL}{settings.WEBHOOK_PATH}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    logger.info(f"Webhook setup at: {webhook_url}")

def remove_webhook():
    """Удаление вебхука (для разработки)"""
    bot.remove_webhook()
    logger.info("Webhook removed")