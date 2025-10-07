from flask import Flask, request
import telebot  # Добавьте этот импорт
from app.bot.bot_core import bot
from app.config import WEBHOOK_URL, WEBHOOK_PATH

app = Flask(__name__)

@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)  # Исправлено: telebot вместо elgbot
        bot.process_new_updates([update])
        return ''
    return 'Invalid content type', 403

def setup_webhook():
    webhook_url = f"{WEBHOOK_URL}{WEBHOOK_PATH}"  # Исправлено: убрали лишний символ >
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == '__main__':
    setup_webhook()
    app.run(host='0.0.0.0', port=8000)