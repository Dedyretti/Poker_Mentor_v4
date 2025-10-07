from telebot.types import ReplyKeyboardMarkup

def get_main_menu():
    """Главное меню бота"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎮 Быстрая игра", "📊 Анализ рук")
    keyboard.row("🎓 Обучение", "📈 Статистика")
    keyboard.row("👤 Мой профиль", "💪 Тренировки")
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


def get_main_menu():
    """Главное меню бота"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎮 Быстрая игра", "📊 Анализ рук")
    keyboard.row("🎓 Обучение", "📈 Статистика")
    keyboard.row("👤 Мой профиль", "💪 Тренировки")
    return keyboard

def get_game_keyboard():
    """Клавиатура для игры"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📊 Инфо о столе", "🎯 Сделать ход")
    keyboard.row("📈 Статистика руки", "🏆 Показать победителя")
    keyboard.row("🔙 Главное меню")
    return keyboard

def get_move_keyboard():
    """Клавиатура для ходов в игре"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("✅ Чек", "📥 Колл (20)")
    keyboard.row("📤 Рейз", "🛑 Фолд")
    keyboard.row("🔙 Назад к игре")
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