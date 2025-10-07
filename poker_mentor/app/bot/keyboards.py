from telebot.types import ReplyKeyboardMarkup

def get_main_menu():
    """Главное меню бота"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎮 Быстрая игра", "📚 Обучение")
    keyboard.row("🔍 Анализ руки", "📈 Статистика")
    keyboard.row("👤 Профиль", "⚙️ Настройки")
    return keyboard

def get_game_keyboard():
    """Клавиатура для игры"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📊 Инфо о столе", "🎯 Сделать ход")
    keyboard.row("📈 Статистика руки", "🏆 Показать победителя")
    keyboard.row("🔙 Главное меню")
    return keyboard

def get_learning_keyboard():
    """Клавиатура для обучения"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📖 Основы покера", "🎯 Стратегии")
    keyboard.row("📊 Анализ рук", "💡 Советы")
    keyboard.row("🔙 Главное меню")
    return keyboard

def get_analysis_keyboard():
    """Клавиатура для анализа руки"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🔄 Проанализировать другую руку")
    keyboard.row("🔙 Главное меню")
    return keyboard