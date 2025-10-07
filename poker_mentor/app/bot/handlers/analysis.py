import telebot
from telebot.handler_backends import State, StatesGroup

class HandAnalysis(StatesGroup):
    waiting_for_hand = State()

def setup_analysis_handlers(bot):
    """Настройка обработчиков для анализа рук"""
    
    @bot.callback_query_handler(func=lambda call: call.data == "analyze_random")
    def analyze_random(callback):
        """Анализ случайной руки"""
        from app.bot.keyboards import get_back_button
        
        analysis_result = """
🎲 <b>Анализ случайной руки:</b>

🃏 Ваша рука: A♠ K♠
🎯 Позиция: Middle Position (MP)
💰 Блайнды: $1/$2

<b>Рекомендации:</b>
✅ <b>Рейз 3x</b> - сильная стартовая рука
📊 <b>Эквити:</b> 45% против случайной руки

<b>Совет:</b> Играйте агрессивно, но будьте готовы к ререйзам
        """
        
        try:
            bot.edit_message_text(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                text=analysis_result,
                reply_markup=get_back_button(),
                parse_mode='HTML'
            )
        except Exception as e:
            bot.send_message(
                callback.message.chat.id,
                analysis_result,
                reply_markup=get_back_button(),
                parse_mode='HTML'
            )
        
        bot.answer_callback_query(callback.id)

    @bot.callback_query_handler(func=lambda call: call.data == "analyze_custom")
    def analyze_custom_start(callback):
        """Начало анализа кастомной руки"""
        from app.bot.keyboards import get_back_button
        
        try:
            bot.edit_message_text(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                text=(
                    "Введите вашу руку в формате: <b>Карта1 Карта2 Позиция</b>\n\n"
                    "Пример: <code>A♠ K♠ MP</code>\n"
                    "Доступные позиции: EP, MP, CO, BTN, SB, BB"
                ),
                reply_markup=get_back_button(),
                parse_mode='HTML'
            )
        except Exception as e:
            bot.send_message(
                callback.message.chat.id,
                (
                    "Введите вашу руку в формате: <b>Карта1 Карта2 Позиция</b>\n\n"
                    "Пример: <code>A♠ K♠ MP</code>\n"
                    "Доступные позиции: EP, MP, CO, BTN, SB, BB"
                ),
                reply_markup=get_back_button(),
                parse_mode='HTML'
            )
        
        bot.set_state(callback.from_user.id, HandAnalysis.waiting_for_hand, callback.message.chat.id)
        bot.answer_callback_query(callback.id)

    @bot.message_handler(state=HandAnalysis.waiting_for_hand)
    def analyze_custom_process(message):
        """Обработка введенной руки"""
        hand_input = message.text.strip()
        
        analysis_result = f"""
🔍 <b>Анализ вашей руки:</b>

🃏 Рука: {hand_input}
🎯 Позиция: Определяется...
💰 Блайнды: $1/$2

<b>Рекомендации:</b>
✅ Анализ выполняется...

<b>Примечание:</b> Функция в стадии разработки
        """
        
        bot.send_message(
            message.chat.id,
            analysis_result,
            parse_mode='HTML'
        )
        
        bot.delete_state(message.from_user.id, message.chat.id)

    @bot.callback_query_handler(func=lambda call: call.data == "back_to_analysis")
    def back_to_analysis(callback):
        """Возврат к меню анализа"""
        from app.bot.keyboards import get_analysis_options_keyboard
        
        analysis_text = "🔍 <b>Анализ покерной руки</b>"
        
        try:
            bot.edit_message_text(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                text=analysis_text,
                reply_markup=get_analysis_options_keyboard(),
                parse_mode='HTML'
            )
        except Exception as e:
            bot.send_message(
                callback.message.chat.id,
                analysis_text,
                reply_markup=get_analysis_options_keyboard(),
                parse_mode='HTML'
            )
        
        bot.answer_callback_query(callback.id)