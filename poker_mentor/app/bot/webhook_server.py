from flask import Flask, request
import telebot  # Добавьте этот импорт
from app.bot.bot_core import bot
from app.config import settings  # ✅ ИСПРАВЛЕННЫЙ ИМПОРТ

app = Flask(__name__)

@app.route(settings.WEBHOOK_PATH, methods=['POST'])  # ✅ settings.WEBHOOK_PATH
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)  # ✅ Update с большой буквы
        bot.process_new_updates([update])
        return ''
    return 'Invalid content type', 403

def setup_webhook():
    webhook_url = f"{settings.WEBHOOK_URL}{settings.WEBHOOK_PATH}"  # ✅ settings
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == '__main__':
    setup_webhook()
    app.run(host='0.0.0.0', port=8000)