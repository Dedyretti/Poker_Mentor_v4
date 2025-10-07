from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.bot.keyboards import get_analysis_options_keyboard, get_back_button

router = Router()

class HandAnalysis(StatesGroup):
    waiting_for_hand = State()

@router.message(Command("analyze"))
@router.message(F.text == "🔍 Анализ руки")
async def cmd_analysis(message: Message):
    """Обработчик анализа руки"""
    analysis_text = """
🔍 <b>Анализ покерной руки</b>

Я могу проанализировать твою покерную руку и дать рекомендации по игре.

Выбери тип анализа:
    """
    
    await message.answer(
        analysis_text,
        reply_markup=get_analysis_options_keyboard()
    )

@router.callback_query(F.data == "analyze_random")
async def analyze_random(callback: CallbackQuery):
    """Анализ случайной руки"""
    # Здесь будет интеграция с AI для анализа
    analysis_result = """
🎲 <b>Анализ случайной руки:</b>

🃏 Ваша рука: A♠ K♠
🎯 Позиция: Middle Position (MP)
💰 Блайнды: $1/$2

<b>Рекомендации:</b>
✅ <b>Рейз 3x</b> - сильная стартовая рука
📊 <b>Эквити:</b> 45% против случайной руки
🎯 <b>Шансы:</b> Хорошие для построения банка

<b>Совет:</b> Играйте агрессивно, но будьте готовы к ререйзам
    """
    
    await callback.message.edit_text(
        analysis_result,
        reply_markup=get_back_button()
    )
    await callback.answer()

@router.callback_query(F.data == "analyze_custom")
async def analyze_custom_start(callback: CallbackQuery, state: FSMContext):
    """Начало анализа кастомной руки"""
    await callback.message.edit_text(
        "Введите вашу руку в формате: <b>Карта1 Карта2 Позиция</b>\n\n"
        "Пример: <code>A♠ K♠ MP</code>\n"
        "Доступные позиции: EP, MP, CO, BTN, SB, BB",
        reply_markup=get_back_button()
    )
    await state.set_state(HandAnalysis.waiting_for_hand)
    await callback.answer()

@router.message(HandAnalysis.waiting_for_hand)
async def analyze_custom_process(message: Message, state: FSMContext):
    """Обработка введенной руки"""
    hand_input = message.text.strip()
    
    # Здесь будет интеграция с AI для анализа
    analysis_result = f"""
🔍 <b>Анализ вашей руки:</b>

🃏 Рука: {hand_input}
🎯 Позиция: MP
💰 Блайнды: $1/$2

<b>Рекомендации:</b>
✅ <b>Результат анализа</b> будет здесь после интеграции с AI

<b>Примечание:</b> Функция анализа в стадии разработки
    """
    
    await message.answer(analysis_result)
    await state.clear()