from typing import Any, Dict

def format_currency(amount: int) -> str:
    """Форматирование денежных сумм"""
    return f"${amount:,}"

def format_percentage(value: float) -> str:
    """Форматирование процентов"""
    return f"{value:.1f}%"

def safe_get(data: Dict, key: str, default: Any = None) -> Any:
    """Безопасное получение значения из словаря"""
    return data.get(key, default)