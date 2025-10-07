from app.bot.bot_core import bot
from app.bot.keyboards import get_main_menu, get_game_keyboard
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

@bot.message_handler(commands=['help'])
def help_command(message):
    """Обработчик команды /help"""
    help_text = """
📖 <b>Помощь по командам:</b>

/start - Запустить бота
/help - Показать эту справку
/profile - Показать профиль
/stats - Статистика игры
/learn - Обучение покеру

<b>Или используйте кнопки меню:</b>
🎮 <b>Быстрая игра</b> - Игра с AI
📊 <b>Анализ рук</b> - Анализ игровых ситуаций
🎓 <b>Обучение</b> - Обучающие материалы
📈 <b>Статистика</b> - Ваша статистика
👤 <b>Мой профиль</b> - Профиль игрока
💪 <b>Тренировки</b> - Упражнения
    """
    bot.send_message(message.chat.id, help_text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "🎮 Быстрая игра")
def start_quick_game(message):
    """Начало быстрой игры"""
    from app.game.game_service import game_service
    
    try:
        # Запускаем быструю игру через game_service
        engine = game_service.start_quick_game(
            telegram_id=str(message.from_user.id),
            user_data={
                'first_name': message.from_user.first_name,
                'username': message.from_user.username
            }
        )
        
        game_state = engine.get_game_state()
        
        game_text = f"""
🎮 <b>Быстрая игра запущена!</b>

🃏 <b>Ваши карты:</b> {' '.join(game_state['players'][0]['hole_cards'])}
💰 <b>Блайнды:</b> {engine.table.blinds['small']}/{engine.table.blinds['big']}
💵 <b>Ваш стек:</b> {game_state['players'][0]['stack']}
🎯 <b>Позиция:</b> {game_state['current_player']}
📊 <b>Стадия:</b> {game_state['state']}

<i>Используйте кнопки ниже для управления игрой! 🎯</i>
        """
        
        bot.send_message(
            message.chat.id,
            game_text,
            reply_markup=get_game_keyboard(),
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error starting quick game: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Произошла ошибка при запуске игры. Попробуйте позже.",
            reply_markup=get_main_menu()
        )

@bot.message_handler(func=lambda message: message.text == "📊 Анализ рук")
def start_analysis(message):
    """Начало анализа руки"""
    analysis_text = """
📊 <b>Профессиональный анализ рук</b>

🔍 <b>Как это работает:</b>
Присылай описание игровой ситуации, и я:

✅ Проанализирую шансы на победу
✅ Оценю силу твоей руки 
✅ Дам рекомендации по ходам
✅ Покажу возможные исходы

📝 <b>Формат запроса:</b>
<code>• Мои карты: A♥ K♥
• Стол: Q♥ J♥ T♥ 2♣ 5♦
• Позиция: Button
• Действия: Колл, Рейз</code>

<i>Присылай свою руку для анализа! 🎯</i>
    """
    bot.send_message(
        message.chat.id,
        analysis_text,
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "🎓 Обучение")
def start_learning(message):
    """Начало обучения"""
    learning_text = """
🎓 <b>Академия покера</b>

📚 <b>Доступные курсы:</b>

🃏 <b>Основы игры</b>
• Правила и комбинации
• Структура торговли
• Позиции за столом

🎯 <b>Префлоп стратегии</b>
• Стартовые руки
• Позиционная игра
• Адаптация к стилям

📊 <b>Постфлоп игра</b>
• Чтение оппонентов
• Управление банкроллом
• Блеф и контроль

💡 <b>Психология</b>
• Тильт-менеджмент
• Принятие решений
• Ментальная игра

<i>Выбери тему для глубокого изучения! 📖</i>
    """
    bot.send_message(
        message.chat.id,
        learning_text,
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "📈 Статистика")
def show_statistics(message):
    """Показать статистику"""
    stats_text = """
📈 <b>Твой покерный паспорт</b>

🏆 <b>Общая статистика:</b>
• 🎮 Сыграно игр: <b>0</b>
• ✅ Успешных рук: <b>0%</b>
• 💰 Средний выигрыш: <b>0</b>
• ⭐ Рейтинг: <b>Новичок</b>

📊 <b>Детальная аналитика:</b>
• 🃏 Префлоп: собирается...
• 📍 Флоп: собирается...
• 🔄 Тёрн: собирается...
• 🏁 Ривер: собирается...

🎯 <b>Рекомендация:</b>
<i>Сыграй 5+ игр для персональной аналитики!</i>
    """
    bot.send_message(
        message.chat.id,
        stats_text,
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == "💪 Тренировки")
def start_training(message):
    """Начало тренировок"""
    training_text = """
💪 <b>Тренировочный режим</b>

🎯 <b>Доступные упражнения:</b>

🧠 <b>Распознавание рук</b>
• Определение силы комбинаций
• Скоростной анализ

📊 <b>Расчет шансов</b> 
• Аутсы и пот оддсы
• Математика покера

🎮 <b>Симуляторы</b>
• Сложные игровые ситуации
• Принятие решений под давлением

📈 <b>Анализ ошибок</b>
• Разбор твоих прошлых игр
• Персональные рекомендации

<i>Выбери тип тренировки для старта! 🔥</i>
    """
    bot.send_message(
        message.chat.id,
        training_text,
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )