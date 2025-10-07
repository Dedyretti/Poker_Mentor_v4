from app.utils.logger import get_logger

logger = get_logger(__name__)

def get_or_create_user(telegram_id: int, username: str = None, first_name: str = None, last_name: str = None):
    """Заглушка для работы с пользователями"""
    logger.info(f"Getting/Creating user: {telegram_id} - {username}")
    return {
        "id": telegram_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name
    }