import os
import logging
import telebot
from dotenv import load_dotenv
from app.config import settings

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

async def start_bot(bot_token: str):
    """Запуск бота в режиме polling"""
    try:
        logger.info("🟢 Запуск бота в режиме polling...")
        setup_handlers()
        print("🟢 Бот запущен и готов к работе!")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise

def setup_handlers():
    """Настройка всех обработчиков"""
    
    @bot.message_handler(commands=['start', 'help'])
    def handle_commands(message):
        from app.bot.keyboards import get_main_menu
        
        if message.text == '/start':
            welcome_text = """
🎯 Добро пожаловать в <b>Poker Mentor</b>!

Используйте кнопки меню ниже для навигации:
• 🎮 Быстрая игра - Начать покерную сессию
• 📊 Анализ рук - Проанализировать руки
• 🎓 Обучение - Изучить стратегии
• 📈 Статистика - Ваша статистика
• 👤 Мой профиль - Настройки профиля
• 💪 Тренировки - Упражнения для улучшения навыков
            """
            bot.send_message(
                message.chat.id,
                welcome_text,
                reply_markup=get_main_menu(),
                parse_mode='HTML'
            )
        else:
            help_text = "📋 Используйте кнопки меню для навигации!"
            bot.send_message(message.chat.id, help_text, reply_markup=get_main_menu())

    # Обработчики для кнопок меню
    @bot.message_handler(func=lambda message: message.text == "🎮 Быстрая игра")
    def start_quick_game(message):
        from app.bot.keyboards import get_game_keyboard
        from app.game.game_service import game_service
        
        try:
            game_service.start_quick_game(
                str(message.from_user.id),
                {
                    'first_name': message.from_user.first_name,
                    'username': message.from_user.username
                }
            )
            
            bot.send_message(
                message.chat.id,
                "🎮 <b>Быстрая игра запущена!</b>\n\nИспользуйте кнопки ниже для управления игрой:",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )
        except Exception as e:
            logger.error(f"Error starting game: {e}")
            bot.send_message(
                message.chat.id,
                "❌ Ошибка при запуске игры. Попробуйте позже."
            )

    # Добавьте остальные обработчики из вашего файла...
    # [Ваши существующие обработчики остаются здесь]

# Настройка обработчиков при импорте
setup_handlers()