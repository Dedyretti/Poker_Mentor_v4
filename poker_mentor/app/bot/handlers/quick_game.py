from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_game_keyboard

@bot.message_handler(func=lambda message: message.text == "📊 Инфо о столе")
def show_table_info(message):
    """Показать информацию о столе"""
    bot.send_message(
        message.chat.id,
        "🎯 Учебный стол\n\n"
        "Игроков: 4\n"
        "Блайнды: 10/20\n"
        "Твой стек: 1500\n"
        "Позиция: Button\n\n"
        "Твои карты: A♥ K♥",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "🎯 Сделать ход")
def make_move(message):
    """Сделать ход"""
    bot.send_message(
        message.chat.id,
        "🎯 Твой ход\n\n"
        "Доступные действия:\n"
        "• ✅ Чек\n" 
        "• 📥 Колл (20)\n"
        "• 📤 Рейз\n"
        "• 🛑 Фолд\n\n"
        "Выбери действие:",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "📈 Статистика руки")
def show_hand_stats(message):
    """Показать статистику руки"""
    bot.send_message(
        message.chat.id,
        "📊 Анализ руки: A♥ K♥\n\n"
        "Шансы на победу: 67%\n"
        "Рекомендуемое действие: Рейз\n"
        "Сила руки: Префлоп монстр",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "🏆 Показать победителя")
def show_winner(message):
    """Показать победителя"""
    bot.send_message(
        message.chat.id,
        "🏆 Победитель раунда!\n\n"
        "Твоя рука: A♥ K♥ - Top Pair\n"
        "Оппонент: Q♥ J♥ - Straight\n\n"
        "Победитель: Оппонент (Straight)\n"
        "Учись на ошибках! 💪",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "🔙 Главное меню")
def return_to_main(message):
    """Вернуться в главное меню"""
    bot.send_message(
        message.chat.id,
        "Возвращаемся в главное меню...",
        reply_markup=get_main_menu()
    )