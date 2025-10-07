from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    """Главное меню бота"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        "🎮 Быстрая игра", "📊 Анализ рук",
        "🎓 Обучение", "📈 Статистика", 
        "👤 Мой профиль", "💪 Тренировки"
    )
    return keyboard

def get_game_keyboard():
    """Клавиатура для игры"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        "📊 Инфо о столе", "🎯 Сделать ход",
        "📈 Статистика руки", "🏆 Показать победителя",
        "🔙 Главное меню"
    )
    return keyboard

def get_move_keyboard():
    """Клавиатура для ходов в игре"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        "✅ Чек", "📥 Колл (20)",
        "📤 Рейз", "🛑 Фолд",
        "🔙 Назад к игре"
    )
    return keyboard

def get_learning_keyboard():
    """Клавиатура для обучения"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        "📖 Основы покера", "🎯 Стратегии",
        "📊 Анализ рук", "💡 Советы",
        "🔙 Главное меню"
    )
    return keyboard

def get_analysis_options_keyboard():
    """Клавиатура с опциями анализа (inline)"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🎲 Анализ случайной руки", callback_data="analyze_random"),
        InlineKeyboardButton("🔍 Анализ своей руки", callback_data="analyze_custom")
    )
    return keyboard

def get_back_button():
    """Кнопка возврата (inline)"""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("⬅️ Назад", callback_data="back_to_analysis"))
    return keyboard