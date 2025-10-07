from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_learning_keyboard, get_game_keyboard, get_analysis_keyboard
from app.database.crud.users import get_or_create_user
from app.utils.logger import get_logger

logger = get_logger(__name__)

@bot.message_handler(commands=['start'])
def start_command(message):
    """Обработчик команды /start"""
    user = message.from_user
    logger.info(f"New user started: {user.id} - {user.username}")
    
    # Создаем или получаем пользователя в БД
    db_user = get_or_create_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )
    
    welcome_text = f"""
👋 Привет, {user.first_name}!

Я - Poker Mentor, твой персональный тренер по покеру! 

🎯 Что я умею:
• 🎮 Проводить учебные игры
• 🔍 Анализировать твои руки
• 📚 Обучать стратегиям
• 📈 Показывать статистику

Выбери действие из меню ниже:
    """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text == "🎮 Быстрая игра")
def start_quick_game(message):
    """Начало быстрой игры"""
    bot.send_message(
        message.chat.id,
        "🎮 Запускаем учебную игру...\n\n"
        "Сейчас я создам виртуальный стол с AI-оппонентами. "
        "Ты сможешь тренироваться в реальных игровых ситуациях!",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "📚 Обучение")
def start_learning(message):
    """Начало обучения"""
    bot.send_message(
        message.chat.id,
        "📚 Раздел обучения\n\n"
        "Выбери тему для изучения:",
        reply_markup=get_learning_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "🔍 Анализ руки")
def start_analysis(message):
    """Начало анализа руки"""
    bot.send_message(
        message.chat.id,
        "🔍 Анализ покерной руки\n\n"
        "Опиши ситуацию в формате:\n"
        "• Твои карты (например, A♥ K♥)\n" 
        "• Карты на столе (например, Q♥ J♥ T♥)\n"
        "• Позиция за столом\n"
        "• Действия оппонентов\n\n"
        "Я проанализирую и дам рекомендации!",
        reply_markup=get_analysis_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "📈 Статистика")
def show_statistics(message):
    """Показать статистику"""
    bot.send_message(
        message.chat.id,
        "📈 Твоя статистика\n\n"
        "Пока данные собираются...\n"
        "Сыграй несколько игр чтобы увидеть свою статистику!",
        reply_markup=get_main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "⚙️ Настройки")
def show_settings(message):
    """Показать настройки"""
    bot.send_message(
        message.chat.id,
        "⚙️ Настройки\n\n"
        "Здесь ты сможешь настроить:\n"
        "• Уровень сложности AI\n"
        "• Тип игры\n"
        "• Уведомления\n\n"
        "Раздел в разработке...",
        reply_markup=get_main_menu()
    )