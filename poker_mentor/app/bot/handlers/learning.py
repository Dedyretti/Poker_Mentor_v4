from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.bot.keyboards import get_learning_keyboard, get_back_button

router = Router()

@router.message(Command("learn"))
@router.message(F.text == "📚 Обучение")
async def cmd_learning(message: Message):
    """Обработчик обучения"""
    learning_text = """
📚 <b>Обучение покеру</b>

Выберите раздел для изучения:

📖 <b>Основы покера</b> - правила и базовые понятия
🎯 <b>Стратегии</b> - тактики игры для разных ситуаций  
💰 <b>Банкролл менеджмент</b> - управление деньгами
🧠 <b>Психология</b> - ментальная сторона игры
📊 <b>Анализ рук</b> - разбор конкретных ситуаций
    """
    
    await message.answer(
        learning_text,
        reply_markup=get_learning_keyboard()
    )

@router.callback_query(F.data == "learn_basics")
async def learn_basics(callback: CallbackQuery):
    """Основы покера"""
    basics_text = """
📖 <b>Основы покера</b>

🎯 <b>Правила Техасского Холдема:</b>
• Каждому игроку сдается 2 карты
• Выкладывается 5 общих карт
• Цель - собрать лучшую комбинацию

🃏 <b>Комбинации (от сильной к слабой):</b>
1. Флеш-рояль
2. Стрит-флеш  
3. Каре
4. Фулл-хаус
5. Флеш
6. Стрит
7. Тройка
8. Две пары
9. Пара
10. Старшая карта

📚 <b>Основные понятия:</b>
• Блайнды - обязательные ставки
• Позиция - порядок хода
• Банк - общие деньги на столе
    """
    
    await callback.message.edit_text(
        basics_text,
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "learn_strategies")
async def learn_strategies(callback: CallbackQuery):
    """Стратегии"""
    strategies_text = """
🎯 <b>Основные стратегии покера</b>

💰 <b>Префлоп стратегия:</b>
• Играйте только сильные руки в ранних позициях
• Расширяйте диапазон в поздних позициях
• Учитывайте действия игроков перед вами

📊 <b>Постфлоп стратегия:</b>
• Продолжайте агрессию с сильными руками
• Будьте осторожны с дро-руками
• Анализируйте текстуру борда

🎭 <b>Позиционная игра:</b>
• BTN - самая сильная позиция
• Используйте позиционное преимущество
• Стелывайте блайнды в поздних позициях
    """
    
    await callback.message.edit_text(
        strategies_text,
        reply_markup=get_back_button()
    )
    await callback.answer()