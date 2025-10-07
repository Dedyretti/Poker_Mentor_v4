import os
import logging
import telebot
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден в .env файле")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# Простые клавиатуры
from telebot.types import ReplyKeyboardMarkup

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎮 Быстрая игра", "📚 Обучение")
    keyboard.row("👤 Профиль", "⚙️ Настройки")
    return keyboard

@bot.message_handler(commands=['start'])
def start_command(message):
    user = message.from_user
    print(f"👤 Новый пользователь: {user.id} - {user.username}")
    
    welcome_text = f"""
👋 Привет, {user.first_name}!

Я - Poker Mentor Bot 🎯

Выбери действие из меню:
    """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.send_message(
        message.chat.id,
        f"🤖 Ты написал: {message.text}\nИспользуй /start для главного меню",
        reply_markup=get_main_menu()
    )

if __name__ == "__main__":
    print("🤖 Запускаем Poker Mentor Bot...")
    print("✅ Бот готов к работе!")
    print("📱 Перейди в Telegram и напиши /start")
    bot.infinity_polling()