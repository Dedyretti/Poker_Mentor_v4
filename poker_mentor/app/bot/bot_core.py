import logging
import telebot
from flask import Flask, request
from app.config import settings

# Инициализация бота
bot = telebot.TeleBot(settings.BOT_TOKEN)

# Flask app для webhook
app = Flask(__name__)

# Настройка логирования
logger = logging.getLogger(__name__)

@ app.route(settings.WEBHOOK_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    return 'Invalid content type', 403

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

def run_webhook():
    """Запуск Flask сервера для webhook"""
    app.run(host='0.0.0.0', port=8000)