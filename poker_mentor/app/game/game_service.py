from typing import Dict, Optional
from .engine import PokerEngine, ActionType
from .table import PokerTable
from .player import Player

class GameService:
    def __init__(self):
        self.active_games = {}

    def start_quick_game(self, telegram_id: str, user_data: Dict) -> PokerEngine:
        table = PokerTable(f"game_{telegram_id}")  # ✅ ИСПРАВЛЕНО: {telegram_id} вместо (telegram_id)

        human_player = Player(telegram_id, user_data.get('first_name', 'Player'), 1000)
        ai_player = Player("ai_1", "AI_Fish", 1000)

        table.add_player(human_player)
        table.add_player(ai_player)

        # Используем простой AI без сложных импортов
        from app.ai.base_ai import FishAI
        fish_ai = FishAI()

        engine = PokerEngine(table, [fish_ai])
        engine.start_new_hand()

        self.active_games[telegram_id] = engine
        return engine

    # Остальные методы остаются без изменений