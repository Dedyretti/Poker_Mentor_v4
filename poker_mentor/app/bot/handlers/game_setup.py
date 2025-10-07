from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.bot.keyboards import get_game_settings_keyboard, get_back_button

router = Router()

@router.message(Command("settings"))
@router.message(F.text == "⚙️ Настройки игры")
async def cmd_game_setup(message: Message):
    """Обработчик настроек игры"""
    settings_text = """
⚙️ <b>Настройки игры</b>

Текущие настройки:
• 💰 Стартовый стек: $1000
• 🎯 Блайнды: $10/$20  
• ⏰ Время на ход: 30 сек
• 🤖 Сложность AI: Средняя

Выберите параметр для изменения:
    """
    
    await message.answer(
        settings_text,
        reply_markup=get_game_settings_keyboard()
    )

@router.callback_query(F.data == "setting_stack")
async def setting_stack(callback: CallbackQuery):
    """Настройка стартового стека"""
    await callback.message.edit_text(
        "💰 <b>Настройка стартового стека</b>\n\n"
        "Введите новый размер стартового стека:\n"
        "• Минимум: $100\n"
        "• Максимум: $10,000\n"
        "• Рекомендуется: $1,000",
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "setting_blinds")
async def setting_blinds(callback: CallbackQuery):
    """Настройка блайндов"""
    await callback.message.edit_text(
        "🎯 <b>Настройка блайндов</b>\n\n"
        "Введите новые блайнды в формате: <code>Малый/Большой</code>\n"
        "Пример: <code>10/20</code>\n\n"
        "Доступные варианты:\n"
        "• 5/10\n• 10/20\n• 25/50\n• 50/100",
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "setting_timing")
async def setting_timing(callback: CallbackQuery):
    """Настройка тайминга"""
    await callback.message.edit_text(
        "⏰ <b>Настройка времени на ход</b>\n\n"
        "Выберите время на обдумывание хода:\n"
        "• 🐇 Быстро: 15 секунд\n"
        "• 🚶 Обычно: 30 секунд\n"
        "• 🐢 Медленно: 60 секунд",
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "setting_difficulty")
async def setting_difficulty(callback: CallbackQuery):
    """Настройка сложности AI"""
    await callback.message.edit_text(
        "🤖 <b>Настройка сложности AI</b>\n\n"
        "Выберите уровень сложности оппонента:\n"
        "• 🟢 Легкий - для новичков\n"
        "• 🟡 Средний - сбалансированная игра\n"
        "• 🔴 Сложный - продвинутые стратегии\n"
        "• 🟣 Эксперт - профессиональный уровень",
        reply_markup=get_back_button()
    )
    await callback.answer()