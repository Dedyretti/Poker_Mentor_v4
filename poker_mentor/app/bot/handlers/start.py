from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.bot.keyboards import get_main_menu_keyboard, get_back_button
from app.database.crud.users import get_or_create_user
from app.database.database import async_session_maker

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    async with async_session_maker() as session:
        user = await get_or_create_user(
            session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name
        )
    
    welcome_text = f"""
👋 Привет, {message.from_user.first_name}!

Добро пожаловать в <b>Poker Mentor</b> - твоего персонального тренера по покеру!

🎯 <b>Что я умею:</b>
• 🎮 Играть с тобой в покер с ИИ
• 🔍 Анализировать твои руки
• 📚 Обучать стратегиям и тактикам
• 📊 Вести статистику твоей игры

Выбери действие из меню ниже:
    """
    
    await message.answer(
        welcome_text,
        reply_markup=get_main_menu_keyboard()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help"""
    help_text = """
📖 <b>Помощь по боту</b>

🎮 <b>Быстрая игра</b> - сыграй партию против ИИ
🔍 <b>Анализ руки</b> - получи анализ своей покерной руки
📚 <b>Обучение</b> - изучи стратегии и тактики покера
👤 <b>Профиль</b> - просмотри свою статистику и достижения
📈 <b>Статистика</b> - детальная аналитика твоей игры
⚙️ <b>Настройки игры</b> - настрой параметры игры

Для начала просто выбери нужный пункт из меню!
    """
    
    await message.answer(help_text)

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    """Обработчик возврата в главное меню"""
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()