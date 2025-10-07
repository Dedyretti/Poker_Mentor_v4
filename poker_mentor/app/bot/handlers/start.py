from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_learning_keyboard, get_game_keyboard, get_analysis_keyboard
from app.database.crud.users import get_or_create_user
from app.utils.logger import get_logger

logger = get_logger(__name__)

@bot.message_handler(commands=['start'])
def start_command(message):
    """Обработчик команды /start"""
    user = message.from_user
    logger.info(f"New user started: {user.id} - {user.username}")
    
    # Создаем или получаем пользователя в БД
    db_user = get_or_create_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )
    
    welcome_text = f"""
🎯 <b>Poker Mentor Pro</b> 🎯

Привет, <b>{user.first_name}</b>! 👋

Я - твой персональный AI-тренер по покеру! 
Прокачивай навыки, анализируй руки и становись профессионалом.

<b>🚀 Мой функционал:</b>

🎮 <b>Быстрая игра</b> - Учебные партии с AI
📊 <b>Анализ рук</b> - Разбор твоих игровых ситуаций  
🎓 <b>Обучение</b> - Стратегии и тактики от профи
📈 <b>Статистика</b> - Твой прогресс и метрики
👤 <b>Профиль</b> - Достижения и рейтинг
💪 <b>Тренировки</b> - Персональные упражнения

<b>Выбери раздел и начнем покерное путешествие! 🃏</b>
    """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu(), parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "🎮 Быстрая игра")
def start_quick_game(message):
    """Начало быстрой игры"""
    from app.bot.keyboards import get_game_keyboard
    
    bot.send_message(
        message.chat.id,
        "🎮 <b>Быстрая игра</b>\n\n"
        "🚀 Запускаю учебный стол...\n\n"
        "📊 <b>Параметры игры:</b>\n"
        "• ♠️ Texas Hold'em\n"
        "• 👥 4 AI-оппонента\n" 
        "• 💰 Блайнды: 10/20\n"
        "• 🎯 Сложность: Средняя\n\n"
        "🎲 <b>Твоя рука:</b> A♥ K♥\n"
        "📍 <b>Позиция:</b> Button\n"
        "💵 <b>Твой стек:</b> 1500\n\n"
        "<i>Используй кнопки ниже для управления игрой! 🎯</i>",
        reply_markup=get_game_keyboard(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "📊 Анализ рук")
def start_analysis(message):
    """Начало анализа руки"""
    bot.send_message(
        message.chat.id,
        "📊 <b>Профессиональный анализ рук</b>\n\n"
        "🔍 <b>Как это работает:</b>\n"
        "Присылай описание игровой ситуации, и я:\n\n"
        "✅ Проанализирую шансы на победу\n"
        "✅ Оценю силу твоей руки\n" 
        "✅ Дам рекомендации по ходам\n"
        "✅ Покажу возможные исходы\n\n"
        "📝 <b>Формат запроса:</b>\n"
        "<code>• Мои карты: A♥ K♥\n"
        "• Стол: Q♥ J♥ T♥ 2♣ 5♦\n"
        "• Позиция: Button\n"
        "• Действия: Колл, Рейз</code>\n\n"
        "<i>Присылай свою руку для анализа! 🎯</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🎓 Обучение")
def start_learning(message):
    """Начало обучения"""
    bot.send_message(
        message.chat.id,
        "🎓 <b>Академия покера</b>\n\n"
        "📚 <b>Доступные курсы:</b>\n\n"
        "🃏 <b>Основы игры</b>\n"
        "• Правила и комбинации\n"
        "• Структура торговли\n"
        "• Позиции за столом\n\n"
        "🎯 <b>Префлоп стратегии</b>\n"
        "• Стартовые руки\n"
        "• Позиционная игра\n"
        "• Адаптация к стилям\n\n"
        "📊 <b>Постфлоп игра</b>\n"
        "• Чтение оппонентов\n"
        "• Управление банкроллом\n"
        "• Блеф и контроль\n\n"
        "💡 <b>Психология</b>\n"
        "• Тильт-менеджмент\n"
        "• Принятие решений\n"
        "• Ментальная игра\n\n"
        "<i>Выбери тему для глубокого изучения! 📖</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "📈 Статистика")
def show_statistics(message):
    """Показать статистику"""
    bot.send_message(
        message.chat.id,
        "📈 <b>Твой покерный паспорт</b>\n\n"
        "🏆 <b>Общая статистика:</b>\n"
        "• 🎮 Сыграно игр: <b>0</b>\n"
        "• ✅ Успешных рук: <b>0%</b>\n"
        "• 💰 Средний выигрыш: <b>0</b>\n"
        "• ⭐ Рейтинг: <b>Новичок</b>\n\n"
        "📊 <b>Детальная аналитика:</b>\n"
        "• 🃏 Префлоп: собирается...\n"
        "• 📍 Флоп: собирается...\n"
        "• 🔄 Тёрн: собирается...\n"
        "• 🏁 Ривер: собирается...\n\n"
        "🎯 <b>Рекомендация:</b>\n"
        "<i>Сыграй 5+ игр для персональной аналитики!</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "💪 Тренировки")
def start_training(message):
    """Начало тренировок"""
    bot.send_message(
        message.chat.id,
        "💪 <b>Тренировочный режим</b>\n\n"
        "🎯 <b>Доступные упражнения:</b>\n\n"
        "🧠 <b>Распознавание рук</b>\n"
        "• Определение силы комбинаций\n"
        "• Скоростной анализ\n\n"
        "📊 <b>Расчет шансов</b>\n" 
        "• Аутсы и пот оддсы\n"
        "• Математика покера\n\n"
        "🎮 <b>Симуляторы</b>\n"
        "• Сложные игровые ситуации\n"
        "• Принятие решений под давлением\n\n"
        "📈 <b>Анализ ошибок</b>\n"
        "• Разбор твоих прошлых игр\n"
        "• Персональные рекомендации\n\n"
        "<i>Выбери тип тренировки для старта! 🔥</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )