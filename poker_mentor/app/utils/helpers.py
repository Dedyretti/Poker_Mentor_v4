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

def format_cards(cards_list):
    """Форматирует список карт для отображения"""
    if not cards_list:
        return "No cards"
    return " ".join(str(card) for card in cards_list)

def format_stack(stack):
    """Форматирует стек игрока"""
    return f"${stack}"

def format_pot(pot):
    """Форматирует банк"""
    return f"Pot: ${pot}"