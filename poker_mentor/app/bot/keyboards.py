from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню"""
    builder = ReplyKeyboardBuilder()
    
    builder.add(KeyboardButton(text="🎮 Быстрая игра"))
    builder.add(KeyboardButton(text="🔍 Анализ руки"))
    builder.add(KeyboardButton(text="📚 Обучение"))
    builder.add(KeyboardButton(text="👤 Профиль"))
    builder.add(KeyboardButton(text="📈 Статистика"))
    builder.add(KeyboardButton(text="⚙️ Настройки игры"))
    
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

def get_game_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура во время игры"""
    builder = ReplyKeyboardBuilder()
    
    builder.add(KeyboardButton(text="📊 Проверить"))
    builder.add(KeyboardButton(text="📈 Поднять"))
    builder.add(KeyboardButton(text="✅ Колл"))
    builder.add(KeyboardButton(text="❌ Фолд"))
    builder.add(KeyboardButton(text="🏳️ Сдаться"))
    builder.add(KeyboardButton(text="📖 Помощь"))
    
    builder.adjust(3, 3)
    return builder.as_markup(resize_keyboard=True)

def get_learning_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для обучения"""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="📖 Основы покера",
        callback_data="learn_basics"
    ))
    builder.add(InlineKeyboardButton(
        text="🎯 Стратегии",
        callback_data="learn_strategies"
    ))
    builder.add(InlineKeyboardButton(
        text="💰 Банкролл менеджмент",
        callback_data="learn_bankroll"
    ))
    builder.add(InlineKeyboardButton(
        text="🧠 Психология",
        callback_data="learn_psychology"
    ))
    builder.add(InlineKeyboardButton(
        text="📊 Анализ рук",
        callback_data="learn_analysis"
    ))
    
    builder.adjust(1)
    return builder.as_markup()

def get_analysis_options_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для опций анализа"""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="🎲 Случайная рука",
        callback_data="analyze_random"
    ))
    builder.add(InlineKeyboardButton(
        text="📝 Ввести руку",
        callback_data="analyze_custom"
    ))
    builder.add(InlineKeyboardButton(
        text="📊 Из истории",
        callback_data="analyze_history"
    ))
    
    builder.adjust(1)
    return builder.as_markup()

def get_game_settings_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для настроек игры"""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="💰 Начальный стек",
        callback_data="setting_stack"
    ))
    builder.add(InlineKeyboardButton(
        text="🎯 Блайнды",
        callback_data="setting_blinds"
    ))
    builder.add(InlineKeyboardButton(
        text="⏰ Тайминг",
        callback_data="setting_timing"
    ))
    builder.add(InlineKeyboardButton(
        text="🤖 Сложность AI",
        callback_data="setting_difficulty"
    ))
    builder.add(InlineKeyboardButton(
        text="💾 Сохранить",
        callback_data="setting_save"
    ))
    
    builder.adjust(2)
    return builder.as_markup()

def get_profile_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура профиля"""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="✏️ Изменить имя",
        callback_data="profile_edit_name"
    ))
    builder.add(InlineKeyboardButton(
        text="📊 История игр",
        callback_data="profile_game_history"
    ))
    builder.add(InlineKeyboardButton(
        text="🏆 Достижения",
        callback_data="profile_achievements"
    ))
    builder.add(InlineKeyboardButton(
        text="⚙️ Настройки",
        callback_data="profile_settings"
    ))
    
    builder.adjust(2)
    return builder.as_markup()

def get_back_button() -> InlineKeyboardMarkup:
    """Кнопка назад"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="⬅️ Назад",
        callback_data="back_to_main"
    ))
    return builder.as_markup()

def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура подтверждения"""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="✅ Да",
        callback_data="confirm_yes"
    ))
    builder.add(InlineKeyboardButton(
        text="❌ Нет",
        callback_data="confirm_no"
    ))
    
    return builder.as_markup()