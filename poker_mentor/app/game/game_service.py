from typing import Dict, Optional
from .engine import PokerEngine, ActionType
from .table import PokerTable
from .player import Player

class GameService:
    def __init__(self):
        self.active_games = {}  # telegram_id -> PokerEngine
    
    def start_quick_game(self, telegram_id: str, user_data: Dict) -> PokerEngine:
        """Начинает быструю игру для пользователя"""
        # Создаем игровой стол
        table = PokerTable(f"game_{telegram_id}")
        
        # Создаем игроков
        human_player = Player(telegram_id, user_data.get('first_name', 'Player'), 1000)
        ai_player = Player("ai_1", "AI_Fish", 1000)
        
        table.add_player(human_player)
        table.add_player(ai_player)
        
        # Создаем AI (импортируем здесь чтобы избежать циклических импортов)
        from app.ai.game_ai import BasePokerAI
        fish_ai = BasePokerAI("fish")
        
        # Создаем движок
        engine = PokerEngine(table, [fish_ai])
        engine.start_new_hand()
        
        # Сохраняем игру
        self.active_games[telegram_id] = engine
        
        return engine
    
    def get_game_state(self, telegram_id: str) -> Optional[Dict]:
        """Возвращает текущее состояние игры"""
        engine = self.active_games.get(telegram_id)
        if engine:
            return engine.get_game_state()
        return None
    
    def make_player_move(self, telegram_id: str, action: str, amount: int = 0) -> bool:
        """Обрабатывает ход игрока"""
        engine = self.active_games.get(telegram_id)
        if not engine:
            return False
        
        # Конвертируем строку в ActionType
        try:
            action_type = ActionType(action.lower())
        except ValueError:
            return False
        
        success = engine.process_player_action(action_type, amount)
        
        # Если после хода человека должен ходить AI - обрабатываем его ход
        if success:
            engine.process_ai_turn()
        
        return success
    
    def get_available_actions(self, telegram_id: str) -> Dict:
        """Возвращает доступные действия для игрока"""
        engine = self.active_games.get(telegram_id)
        if not engine:
            return {}
        
        current_player = engine.get_current_player()
        if not current_player or str(current_player.player_id) != str(telegram_id):
            return {}
        
        game_state = engine.get_game_state()
        current_bet = game_state.get('current_bet', 0)
        player_bet = current_player.current_bet
        
        actions = {
            "fold": True,
            "check": player_bet >= current_bet,
            "call": player_bet < current_bet and current_bet - player_bet <= current_player.stack,
            "raise": current_player.stack > current_bet
        }
        
        return actions

# Глобальный экземпляр сервиса
game_service = GameService()

# python tests/test_game/test_ai_integration.py