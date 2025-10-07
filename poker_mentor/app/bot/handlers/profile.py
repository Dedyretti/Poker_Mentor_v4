from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu

@bot.message_handler(func=lambda message: message.text == "👤 Профиль")
def show_profile(message):
    """Показать профиль пользователя"""
    bot.send_message(
        message.chat.id,
        "👤 Твой профиль:\n\n"
        "📊 Игр сыграно: 0\n"
        "🏆 Побед: 0\n"
        "⭐ Рейтинг: Новичок\n\n"
        "Пока статистика собирается...",
        reply_markup=get_main_menu()
    )