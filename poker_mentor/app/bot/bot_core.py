import os
import logging
import telebot
from dotenv import load_dotenv



import os
import logging
import telebot
from dotenv import load_dotenv
from app.config import settings  # ✅ ДОБАВЛЕН ИМПОРТ

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)  # ✅ settings вместо os.getenv
dp = bot  # для совместимости

# ... остальной код без изменений ...

def start_bot(use_webhook=False):  # ✅ use_webhook=False по умолчанию
    """Запуск бота"""
    try:
        if use_webhook:
            logger.info("Запуск в режиме webhook...")
            # Код для webhook
        else:
            logger.info("Запуск в режиме polling...")  # ✅ ЭТО ДОЛЖНО БЫТЬ ПО УМОЛЧАНИЮ
            setup_handlers()
            print("🟢 Бот запущен и готов к работе!")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)  # ✅ POLLING
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")

def setup_handlers():
    """Настройка всех обработчиков"""
    
    # ОБРАБОТЧИК КОМАНД /start и /help
    @bot.message_handler(commands=['start', 'help'])
    def handle_commands(message):
        from app.bot.keyboards import get_main_menu
        
        if message.text == '/start':
            welcome_text = """
🎯 Добро пожаловать в <b>Poker Mentor</b>!

Используйте кнопки меню ниже для навигации:
• 🎮 Быстрая игра - Начать покерную сессию
• 📊 Анализ рук - Проанализировать руки
• 🎓 Обучение - Изучить стратегии
• 📈 Статистика - Ваша статистика
• 👤 Мой профиль - Настройки профиля
• 💪 Тренировки - Упражнения для улучшения навыков
            """
            bot.send_message(
                message.chat.id,
                welcome_text,
                reply_markup=get_main_menu(),
                parse_mode='HTML'
            )
        else:
            help_text = "📋 Используйте кнопки меню для навигации!"
            bot.send_message(message.chat.id, help_text, reply_markup=get_main_menu())

    # ЕДИНСТВЕННЫЙ обработчик для ВСЕХ текстовых сообщений
    @bot.message_handler(content_types=['text'])
    def handle_all_messages(message):
        from app.bot.keyboards import (
            get_main_menu, get_game_keyboard, get_analysis_options_keyboard,
            get_learning_keyboard, get_move_keyboard
        )
        
        text = message.text
        user_id = str(message.from_user.id)
        
        print(f"🎯 Обрабатываем текст: '{text}' от пользователя {user_id}")

        # Главное меню
        if text == "🎮 Быстрая игра":
            print("🎮 Запускаем быструю игру")
            bot.send_message(
                message.chat.id,
                "🎮 <b>Запускаем быструю игру...</b>\n\nСоздаем игровой стол...",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )
            
            # Имитация создания игры
            import time
            time.sleep(1)
            
            bot.send_message(
                message.chat.id,
                "✅ <b>Игра создана!</b>\n\n"
                "Стол: $1/$2 No-Limit Hold'em\n"
                "Игроков: 2\n"
                "Ваш стек: $1000\n\n"
                "🃏 Ваши карты: A♠ K♥\n"
                "💰 Текущий банк: $3\n\n"
                "Выберите действие в меню ниже:",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "📊 Анализ рук":
            print("📊 Открываем анализ рук")
            analysis_text = "🔍 <b>Анализ покерной руки</b>\n\nВыберите тип анализа:"
            bot.send_message(
                message.chat.id,
                analysis_text,
                reply_markup=get_analysis_options_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🎓 Обучение":
            print("🎓 Открываем обучение")
            bot.send_message(
                message.chat.id,
                "🎓 <b>Раздел обучения</b>\n\nВыберите тему для изучения:",
                reply_markup=get_learning_keyboard(),
                parse_mode='HTML'
            )

        elif text == "📈 Статистика":
            print("📈 Открываем статистику")
            bot.send_message(
                message.chat.id,
                "📈 <b>Ваша статистика</b>\n\nРаздел в разработке...",
                reply_markup=get_main_menu(),
                parse_mode='HTML'
            )

        elif text == "👤 Мой профиль":
            print("👤 Открываем профиль")
            bot.send_message(
                message.chat.id,
                "👤 <b>Мой профиль</b>\n\nРаздел в разработке...",
                reply_markup=get_main_menu(),
                parse_mode='HTML'
            )

        elif text == "💪 Тренировки":
            print("💪 Открываем тренировки")
            bot.send_message(
                message.chat.id,
                "💪 <b>Тренировки</b>\n\nРаздел в разработке...",
                reply_markup=get_main_menu(),
                parse_mode='HTML'
            )

        # Игровое меню
        elif text == "📊 Инфо о столе":
            print("📊 Показываем инфо о столе")
            bot.send_message(
                message.chat.id,
                "📊 <b>Информация о столе:</b>\n\n"
                "Стол: $1/$2 No-Limit Hold'em\n"
                "Игроков: 2/2\n"
                "Ваш стек: $1000\n"
                "Позиция: Button\n"
                "Текущий банк: $3\n\n"
                "🃏 Ваши карты: A♠ K♥\n"
                "🤖 Оппонент: $980",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🎯 Сделать ход":
            print("🎯 Показываем ходы")
            bot.send_message(
                message.chat.id,
                "🎯 <b>Ваш ход</b>\n\n"
                "Ваша рука: A♠ K♥\n"
                "Доска: Пока нет общих карт\n"
                "Банк: $3\n"
                "Текущая ставка: $2\n\n"
                "Выберите действие:",
                reply_markup=get_move_keyboard(),
                parse_mode='HTML'
            )

        elif text == "✅ Чек":
            print("✅ Обрабатываем чек")
            bot.send_message(
                message.chat.id,
                "✅ Вы сделали чек\n\n"
                "🤖 Оппонент делает рейз до $10",
                reply_markup=get_move_keyboard(),
                parse_mode='HTML'
            )

        elif text == "📥 Колл (20)":
            print("📥 Обрабатываем колл")
            bot.send_message(
                message.chat.id,
                "📥 Вы поставили колл $20\n\n"
                "🤖 Оппонент делает чек",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "📤 Рейз":
            print("📤 Обрабатываем рейз")
            bot.send_message(
                message.chat.id,
                "📤 Вы сделали рейз до $40\n\n"
                "🤖 Оппонент фолдит\n"
                "🏆 Вы выиграли банк $45!",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🛑 Фолд":
            print("🛑 Обрабатываем фолд")
            bot.send_message(
                message.chat.id,
                "🛑 Вы сбросили карты\n\n"
                "🤖 Оппонент выиграл банк $3",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "📈 Статистика руки":
            print("📈 Показываем статистику руки")
            bot.send_message(
                message.chat.id,
                "📈 <b>Статистика руки:</b>\n\n"
                "Эквити: ~67%\n"
                "Ауты: 6 (2 туза + 4 короля)\n"
                "Шансы улучшения: 24%\n"
                "Рекомендация: Агрессивная игра",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🏆 Показать победителя":
            print("🏆 Показываем победителя")
            bot.send_message(
                message.chat.id,
                "🏆 <b>Победитель раунда!</b>\n\n"
                "Победитель: Вы! 🎉\n"
                "Комбинация: Топ-пара с лучшим кикером\n"
                "Выигрыш: $45\n"
                "Новый стек: $1045",
                reply_markup=get_game_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🔙 Главное меню":
            print("🔙 Возврат в главное меню")
            bot.send_message(
                message.chat.id,
                "🔄 Возвращаемся в главное меню...",
                reply_markup=get_main_menu()
            )

        elif text == "🔙 Назад к игре":
            print("🔙 Возврат к игре")
            bot.send_message(
                message.chat.id,
                "🔄 Возврат к игровому меню...",
                reply_markup=get_game_keyboard()
            )

        # Обучение
        elif text == "📖 Основы покера":
            bot.send_message(
                message.chat.id,
                "📖 <b>Основы покера:</b>\n\n"
                "Текс-ас Холдем - самая популярная покерная игра.\n"
                "Каждый игрок получает 2 карты, затем выкладываются 5 общих карт.\n"
                "Цель - собрать лучшую комбинацию из 5 карт.",
                reply_markup=get_learning_keyboard(),
                parse_mode='HTML'
            )

        elif text == "🎯 Стратегии":
            bot.send_message(
                message.chat.id,
                "🎯 <b>Основные стратегии:</b>\n\n"
                "• Позиционная игра\n"
                "• Выбор стартовых рук\n"
                "• Управление банкроллом\n"
                "• Чтение оппонентов",
                reply_markup=get_learning_keyboard(),
                parse_mode='HTML'
            )

        elif text == "💡 Советы":
            bot.send_message(
                message.chat.id,
                "💡 <b>Полезные советы:</b>\n\n"
                "• Играйте меньше рук, но более агрессивно\n"
                "• Обращайте внимание на позицию\n"
                "• Изучайте математику покера\n"
                "• Анализируйте свои раздачи",
                reply_markup=get_learning_keyboard(),
                parse_mode='HTML'
            )

        else:
            print(f"❌ Неизвестная команда: '{text}'")
            bot.send_message(
                message.chat.id,
                "❓ Неизвестная команда. Используйте кнопки меню для навигации",
                reply_markup=get_main_menu()
            )

    # Обработчики callback-запросов (для inline кнопок)
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        print(f"🔘 Callback: {call.data}")
        bot.answer_callback_query(call.id)

# Настройка обработчиков при импорте
setup_handlers()