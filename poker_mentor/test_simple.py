import os
import telebot
from dotenv import load_dotenv

load_dotenv()

# Создаем бота напрямую
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, 
        "🎯 Poker Mentor Bot работает!\n\n"
        "Используй /start для начала работы"
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(
        message.chat.id, 
        f"Вы сказали: {message.text}\n\n"
        "Используй /start для главного меню"
    )

if __name__ == "__main__":
    print("🤖 Запускаем простого бота для теста...")
    bot.infinity_polling()