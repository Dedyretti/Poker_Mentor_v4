from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.bot.keyboards import get_game_keyboard, get_back_button
from app.database.redis_client import redis_client

router = Router()

@router.message(Command("game"))
@router.message(F.text == "🎮 Быстрая игра")
async def cmd_quick_game(message: Message):
    """Обработчик быстрой игры"""
    game_text = """
🎮 <b>Быстрая игра против ИИ</b>

Настройки игры:
• 💰 Стартовый стек: $1000
• 🎯 Блайнды: $10/$20
• 🤖 Сложность: Средняя

Готов начать игру?
    """
    
    await message.answer(
        game_text,
        reply_markup=get_game_keyboard()
    )

@router.message(F.text == "📊 Проверить")
async def game_check(message: Message):
    """Проверить в игре"""
    # Здесь будет интеграция с игровым движком
    await message.answer("Вы проверяете... Ход переходит к следующему игроку.")

@router.message(F.text == "📈 Поднять")
async def game_raise(message: Message):
    """Поднять в игре"""
    await message.answer("Вы поднимаете... Введите сумму:")

@router.message(F.text == "✅ Колл")
async def game_call(message: Message):
    """Колл в игре"""
    await message.answer("Вы делаете колл...")

@router.message(F.text == "❌ Фолд")
async def game_fold(message: Message):
    """Фолд в игре"""
    await message.answer("Вы сбрасываете карты...")

@router.message(F.text == "🏳️ Сдаться")
async def game_surrender(message: Message):
    """Сдаться в игре"""
    await message.answer("Вы сдались. Игра окончена.")

@router.message(F.text == "📖 Помощь")
async def game_help(message: Message):
    """Помощь во время игры"""
    help_text = """
📖 <b>Помощь во время игры</b>

📊 <b>Проверить</b> - пропустить ход
📈 <b>Поднять</b> - увеличить ставку
✅ <b>Колл</b> - принять текущую ставку  
❌ <b>Фолд</b> - сбросить карты
🏳️ <b>Сдаться</b> - завершить игру досрочно

Используйте эти команды для управления игрой!
    """
    
    await message.answer(help_text)