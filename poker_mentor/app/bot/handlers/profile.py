from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu

@bot.message_handler(func=lambda message: message.text == "👤 Мой профиль")
def show_profile(message):
    """Показать профиль пользователя"""
    bot.send_message(
        message.chat.id,
        "👤 <b>Твой покерный профиль</b>\n\n"
        "📅 <b>Активность:</b>\n"
        "• 🎮 Сыграно игр: <b>0</b>\n"
        "• 🏆 Побед: <b>0</b>\n"
        "• ⏱️ В игре: <b>0 минут</b>\n\n"
        "💰 <b>Банкролл:</b>\n"
        "• Виртуальный: <b>1000 фишек</b>\n"
        "• Изменение: <b>+0%</b>\n\n"
        "🎯 <b>Достижения:</b>\n"
        "• 🥇 Первая игра\n"
        "• 📚 Ученик покера\n"
        "• 💪 Стабильный игрок\n\n"
        "⭐ <b>Твой уровень:</b> <i>Новичок</i>\n\n"
        "<i>Продолжай в том же духе! 🚀</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )