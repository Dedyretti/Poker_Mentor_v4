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
    """Сделать ход - показать доступные действия"""
    bot.send_message(
        message.chat.id,
        "🎯 <b>Твой ход</b>\n\n"
        "📊 <b>Текущая ситуация:</b>\n"
        "• Банк: 30 фишек\n"
        "• Ставка: 20 фишек\n"
        "• Твоя позиция: Button\n\n"
        "🃏 <b>Твоя рука:</b> A♥ K♥\n"
        "📈 <b>Шансы на победу:</b> 67%\n\n"
        "<b>Выбери действие:</b>",
        reply_markup=get_move_keyboard(),  # ← ЭТА СТРОКА ОБЯЗАТЕЛЬНА!
        parse_mode='HTML'
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

from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_game_keyboard, get_move_keyboard

@bot.message_handler(func=lambda message: message.text == "📊 Инфо о столе")
def show_table_info(message):
    """Показать информацию о столе"""
    bot.send_message(
        message.chat.id,
        "🎯 <b>Учебный стол</b>\n\n"
        "👥 Игроков: 4\n"
        "💰 Блайнды: 10/20\n"
        "💵 Твой стек: 1500\n"
        "📍 Позиция: Button\n\n"
        "🃏 <b>Твои карты:</b> A♥ K♥\n\n"
        "<i>Отличная стартовая рука! 💪</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🎯 Сделать ход")
def make_move(message):
    """Сделать ход - показать доступные действия"""
    bot.send_message(
        message.chat.id,
        "🎯 <b>Твой ход</b>\n\n"
        "📊 <b>Текущая ситуация:</b>\n"
        "• Банк: 30 фишек\n"
        "• Ставка: 20 фишек\n"
        "• Твоя позиция: Button\n\n"
        "🃏 <b>Твоя рука:</b> A♥ K♥\n"
        "📈 <b>Шансы на победу:</b> 67%\n\n"
        "<b>Выбери действие:</b>",
        reply_markup=get_move_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "✅ Чек")
def check_move(message):
    """Обработчик чека"""
    bot.send_message(
        message.chat.id,
        "✅ <b>Ты сделал ЧЕК</b>\n\n"
        "Ход переходит следующему игроку.\n"
        "Ждем действий оппонентов...\n\n"
        "<i>Стратегическое ожидание! 🎯</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "📥 Колл (20)")
def call_move(message):
    """Обработчик колла"""
    bot.send_message(
        message.chat.id,
        "📥 <b>Ты сделал КОЛЛ (20 фишек)</b>\n\n"
        "Ты уравнял ставку и остался в игре.\n"
        "Банк увеличился до 50 фишек.\n\n"
        "<i>Солидное решение! 💰</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "📤 Рейз")
def raise_move(message):
    """Обработчик рейза"""
    bot.send_message(
        message.chat.id,
        "📤 <b>Ты сделал РЕЙЗ до 60 фишек</b>\n\n"
        "Агрессивная игра! 💪\n"
        "Ты увеличил ставку в 3 раза.\n"
        "Банк: 90 фишек\n\n"
        "<i>Оппоненты в замешательстве! 😮</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🛑 Фолд")
def fold_move(message):
    """Обработчик фолда"""
    bot.send_message(
        message.chat.id,
        "🛑 <b>Ты сделал ФОЛД</b>\n\n"
        "Ты сбросил карты и вышел из раздачи.\n"
        "Сохранил 20 фишек для следующей игры.\n\n"
        "<i>Иногда отступление - лучшая стратегия! 🎯</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🔙 Назад к игре")
def back_to_game(message):
    """Вернуться к игровому меню"""
    bot.send_message(
        message.chat.id,
        "🔄 Возвращаемся к обзору игры...",
        reply_markup=get_game_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "📈 Статистика руки")
def show_hand_stats(message):
    """Показать статистику руки"""
    bot.send_message(
        message.chat.id,
        "📊 <b>Анализ руки: A♥ K♥</b>\n\n"
        "🎯 <b>Шансы на победу:</b> 67%\n"
        "💪 <b>Сила руки:</b> Префлоп монстр\n"
        "⭐ <b>Рейтинг:</b> Топ 3% стартовых рук\n\n"
        "📈 <b>Рекомендации:</b>\n"
        "• Префлоп: Агрессивный рейз\n"
        "• Постфлоп: Продолжать агрессию\n"
        "• Против ререйза: Колл/Рейз\n\n"
        "<i>Играй смело! Эта рука того стоит 🚀</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🏆 Показать победителя")
def show_winner(message):
    """Показать победителя"""
    bot.send_message(
        message.chat.id,
        "🏆 <b>Результат раздачи!</b>\n\n"
        "🃏 <b>Твоя рука:</b> A♥ K♥ - Top Pair, Top Kicker\n"
        "👥 <b>Оппонент:</b> Q♥ J♥ - Straight\n"
        "📊 <b>Борд:</b> T♥ 9♣ 8♦ 2♣ 7♥\n\n"
        "🎯 <b>Победитель:</b> Оппонент (Straight)\n"
        "💰 <b>Выигрыш:</b> 90 фишек\n\n"
        "💡 <b>Анализ:</b>\n"
        "Ты правильно играл сильную руку,\n"
        "но оппоненту повезло со стритом.\n\n"
        "<i>Такое бывает в покере! Учись на ошибках 💪</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🔙 Главное меню")
def return_to_main(message):
    """Вернуться в главное меню"""
    bot.send_message(
        message.chat.id,
        "🔙 Возвращаемся в главное меню...",
        reply_markup=get_main_menu()
    )