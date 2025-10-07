from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.bot.keyboards import get_back_button

router = Router()

@router.message(Command("stats"))
@router.message(F.text == "📈 Статистика")
async def cmd_statistics(message: Message):
    """Обработчик статистики"""
    stats_text = """
📊 <b>Детальная статистика</b>

🎮 <b>Общая статистика:</b>
• Всего игр: 25
• Побед: 15 (60%)
• Поражений: 10 (40%)

💰 <b>Финансовая статистика:</b>
• Общий выигрыш: $2,450
• Общий проигрыш: $1,890
• Чистая прибыль: $560
• ROI: 29.6%

🎯 <b>Статистика по позициям:</b>
• BTN: 65% побед
• CO: 58% побед
• MP: 52% побед
• EP: 48% побед

📈 <b>График прогресса:</b>
(график будет отображаться здесь)
    """
    
    await message.answer(stats_text)

@router.callback_query(F.data == "stats_detailed")
async def stats_detailed(callback: CallbackQuery):
    """Детальная статистика"""
    detailed_stats = """
📈 <b>Детальная аналитика</b>

🃏 <b>Статистика по рукам:</b>
• AA: 85% побед
• KK: 78% побед  
• QQ: 72% побед
• AK: 65% побед

⏰ <b>По времени суток:</b>
• Утро: 45% побед
• День: 60% побед
• Вечер: 55% побед
• Ночь: 70% побед

📅 <b>По неделям:</b>
• Неделя 1: 50% побед
• Неделя 2: 55% побед
• Неделя 3: 65% побед
• Неделя 4: 70% побед
    """
    
    await callback.message.edit_text(
        detailed_stats,
        reply_markup=get_back_button()
    )
    await callback.answer()