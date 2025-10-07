import os
import logging
import telebot
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден в .env файле")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# Простые клавиатуры
from telebot.types import ReplyKeyboardMarkup

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎮 Быстрая игра", "📊 Анализ рук")
    keyboard.row("🎓 Обучение", "📈 Статистика")
    keyboard.row("👤 Мой профиль", "💪 Тренировки")
    return keyboard

@bot.message_handler(commands=['start'])
def start_command(message):
    user = message.from_user
    print(f"👤 Новый пользователь: {user.id} - {user.username}")
    
    welcome_text =  f"""
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
⚙️ <b>Тренировки</b> - Персональные упражнения

<b>Выбери раздел и начнем покерное путешествие! 🃏</b>
    """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text in ["🎮 Быстрая игра", "💬 Быстрая игра"])
def quick_game(message):
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
        "<i>Готов к покерной битве? 💥</i>",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text in ["📊 Анализ рук", "💬 Анализ рук"])
def analysis(message):
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

@bot.message_handler(func=lambda message: message.text in ["🎓 Обучение", "💬 Обучение"]) 
def learning(message):
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

@bot.message_handler(func=lambda message: message.text in ["📈 Статистика", "💬 Статистика"])
def statistics(message):
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

@bot.message_handler(func=lambda message: message.text in ["👤 Мой профиль", "💬 Мой профиль"])
def profile(message):
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

@bot.message_handler(func=lambda message: message.text in ["💪 Тренировки", "💬 Тренировки"])
def training(message):
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

if __name__ == "__main__":
    print("🤖 Запускаем Poker Mentor Bot...")
    print("✅ Бот готов к работе!")
    print("📱 Перейди в Telegram и напиши /start")
    bot.infinity_polling()