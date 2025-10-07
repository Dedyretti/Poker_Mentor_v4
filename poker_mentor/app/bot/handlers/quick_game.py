from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_game_keyboard, get_move_keyboard
from app.game.game_service import game_service
from app.utils.logger import get_logger

logger = get_logger(__name__)

@bot.message_handler(func=lambda message: message.text == "📊 Инфо о столе")
def show_table_info(message):
    """Показать информацию о столе"""
    try:
        game_state = game_service.get_game_state(str(message.from_user.id))
        
        if not game_state:
            bot.send_message(
                message.chat.id,
                "❌ У вас нет активной игры. Начните новую игру!",
                reply_markup=get_main_menu()
            )
            return
        
        player_info = game_state['players'][0]  # Первый игрок - пользователь
        
        table_text = f"""
🎯 <b>Учебный стол</b>

👥 Игроков: {len(game_state['players'])}
💰 Блайнды: {game_state.get('small_blind', 10)}/{game_state.get('big_blind', 20)}
💵 Твой стек: {player_info['stack']}
📍 Позиция: {game_state['current_player']}
📊 Стадия: {game_state['state']}

🃏 <b>Твои карты:</b> {' '.join(player_info['hole_cards']) if player_info['hole_cards'] else 'Скрыто'}

<i>Отличная стартовая рука! 💪</i>
        """
        
        bot.send_message(
            message.chat.id,
            table_text,
            reply_markup=get_game_keyboard(),
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error showing table info: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при получении информации о столе.",
            reply_markup=get_main_menu()
        )

@bot.message_handler(func=lambda message: message.text == "🎯 Сделать ход")
def make_move(message):
    """Сделать ход - показать доступные действия"""
    try:
        game_state = game_service.get_game_state(str(message.from_user.id))
        
        if not game_state:
            bot.send_message(
                message.chat.id,
                "❌ У вас нет активной игры. Начните новую игру!",
                reply_markup=get_main_menu()
            )
            return
        
        # Получаем доступные действия
        available_actions = game_service.get_available_actions(str(message.from_user.id))
        
        actions_text = "Доступные действия:\n"
        for action, available in available_actions.items():
            if available:
                actions_text += f"• {action.upper()}\n"
        
        move_text = f"""
🎯 <b>Твой ход</b>

📊 <b>Текущая ситуация:</b>
• Банк: {game_state['pot']} фишек
• Стадия: {game_state['state']}
• Твоя позиция: {game_state['current_player']}

🃏 <b>Твоя рука:</b> {' '.join(game_state['players'][0]['hole_cards'])}
📈 <b>Доступные действия:</b>
{actions_text}

<b>Выбери действие:</b>
        """
        
        bot.send_message(
            message.chat.id,
            move_text,
            reply_markup=get_move_keyboard(),
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error in make_move: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при получении доступных действий.",
            reply_markup=get_game_keyboard()
        )

# Обработчики игровых действий
@bot.message_handler(func=lambda message: message.text == "✅ Чек")
def check_move(message):
    """Обработчик чека"""
    try:
        success = game_service.make_player_move(str(message.from_user.id), "check")
        
        if success:
            bot.send_message(
                message.chat.id,
                "✅ <b>Ты сделал ЧЕК</b>\n\n"
                "Ход переходит следующему игроку.\n"
                "Ждем действий оппонентов...\n\n"
                "<i>Стратегическое ожидание! 🎯</i>",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Невозможно сделать чек в текущей ситуации.",
                reply_markup=get_move_keyboard()
            )
            
    except Exception as e:
        logger.error(f"Error in check_move: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при выполнении действия.",
            reply_markup=get_game_keyboard()
        )

@bot.message_handler(func=lambda message: message.text == "📥 Колл (20)")
def call_move(message):
    """Обработчик колла"""
    try:
        success = game_service.make_player_move(str(message.from_user.id), "call", 20)
        
        if success:
            bot.send_message(
                message.chat.id,
                "📥 <b>Ты сделал КОЛЛ (20 фишек)</b>\n\n"
                "Ты уравнял ставку и остался в игре.\n"
                "Банк увеличился до 50 фишек.\n\n"
                "<i>Солидное решение! 💰</i>",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Невозможно сделать колл в текущей ситуации.",
                reply_markup=get_move_keyboard()
            )
            
    except Exception as e:
        logger.error(f"Error in call_move: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при выполнении действия.",
            reply_markup=get_game_keyboard()
        )

@bot.message_handler(func=lambda message: message.text == "📤 Рейз")
def raise_move(message):
    """Обработчик рейза"""
    try:
        success = game_service.make_player_move(str(message.from_user.id), "raise", 60)
        
        if success:
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
        else:
            bot.send_message(
                message.chat.id,
                "❌ Невозможно сделать рейз в текущей ситуации.",
                reply_markup=get_move_keyboard()
            )
            
    except Exception as e:
        logger.error(f"Error in raise_move: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при выполнении действия.",
            reply_markup=get_game_keyboard()
        )

@bot.message_handler(func=lambda message: message.text == "🛑 Фолд")
def fold_move(message):
    """Обработчик фолда"""
    try:
        success = game_service.make_player_move(str(message.from_user.id), "fold")
        
        if success:
            bot.send_message(
                message.chat.id,
                "🛑 <b>Ты сделал ФОЛД</b>\n\n"
                "Ты сбросил карты и вышел из раздачи.\n"
                "Сохранил 20 фишек для следующей игры.\n\n"
                "<i>Иногда отступление - лучшая стратегия! 🎯</i>",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Невозможно сделать фолд в текущей ситуации.",
                reply_markup=get_move_keyboard()
            )
            
    except Exception as e:
        logger.error(f"Error in fold_move: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Ошибка при выполнении действия.",
            reply_markup=get_game_keyboard()
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