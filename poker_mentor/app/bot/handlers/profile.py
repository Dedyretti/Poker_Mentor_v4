from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.bot.keyboards import get_profile_keyboard, get_back_button
from app.database.crud.users import get_user_profile
from app.database.database import async_session_maker

router = Router()

@router.message(Command("profile"))
@router.message(F.text == "👤 Профиль")
async def cmd_profile(message: Message):
    """Обработчик профиля пользователя"""
    async with async_session_maker() as session:
        profile = await get_user_profile(session, message.from_user.id)
    
    if not profile:
        await message.answer("Профиль не найден")
        return
    
    profile_text = f"""
👤 <b>Профиль игрока</b>

📛 Имя: {profile['first_name']} {profile.get('last_name', '')}
🎯 Уровень: {profile.get('level', 'Новичок')}
🏆 Опыт: {profile.get('experience', 0)} XP

📊 <b>Статистика:</b>
🎮 Сыграно игр: {profile.get('games_played', 0)}
✅ Побед: {profile.get('wins', 0)}
📈 Винрейт: {profile.get('win_rate', 0)}%

💰 <b>Банкролл:</b>
💵 Текущий: ${profile.get('bankroll', 0)}
📈 Максимальный: ${profile.get('max_bankroll', 0)}
    """
    
    await message.answer(
        profile_text,
        reply_markup=get_profile_keyboard()
    )

@router.callback_query(F.data == "profile_edit_name")
async def profile_edit_name(callback: CallbackQuery):
    """Редактирование имени"""
    await callback.message.edit_text(
        "Введите новое имя:",
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "profile_game_history")
async def profile_game_history(callback: CallbackQuery):
    """История игр"""
    # Здесь будет интеграция с БД для получения истории
    history_text = "📊 <b>История последних игр:</b>\n\n(функция в разработке)"
    
    await callback.message.edit_text(
        history_text,
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "profile_achievements")
async def profile_achievements(callback: CallbackQuery):
    """Достижения"""
    achievements_text = """
🏆 <b>Достижения:</b>

🎯 <b>Первый шаг</b> - Сыграть первую игру
💰 <b>Банкролл менеджер</b> - Достичь банкролла $1000
🏅 <b>Победитель</b> - Выиграть 10 игр
📚 <b>Ученик</b> - Пройти 5 уроков
    """
    
    await callback.message.edit_text(
        achievements_text,
        reply_markup=get_back_button()
    )
    await callback.answer()