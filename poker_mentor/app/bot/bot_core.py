from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.handlers import (
    start,
    profile,
    statistics,
    analysis,
    quick_game,
    game_setup,
    learning
)
from app.config import settings

async def setup_bot(bot: Bot, dp: Dispatcher):
    """Настройка бота и регистрация handlers"""
    
    # Регистрация routers
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(statistics.router)
    dp.include_router(analysis.router)
    dp.include_router(quick_game.router)
    dp.include_router(game_setup.router)
    dp.include_router(learning.router)
    
    # Настройка вебхука (если указан)
    if settings.WEBHOOK_URL:
        await setup_webhook(bot)

async def setup_webhook(bot: Bot):
    """Настройка вебхука для продакшена"""
    webhook_url = f"{settings.WEBHOOK_URL}{settings.WEBHOOK_PATH}"
    await bot.set_webhook(
        url=webhook_url,
        drop_pending_updates=True
    )

async def delete_webhook(bot: Bot):
    """Удаление вебхука (для разработки)"""
    await bot.delete_webhook(drop_pending_updates=True)