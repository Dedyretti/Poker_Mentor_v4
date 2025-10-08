from abc import ABC, abstractmethod
from typing import Dict, List
from app.game.engine import ActionType

class BasePokerAI(ABC):
    def __init__(self, ai_type: str):
        self.ai_type = ai_type
        self.aggression_factor = 1.0
        self.fold_threshold = 0.7
    
    @abstractmethod
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        """Принять решение о действии"""
        pass

class FishAI(BasePokerAI):
    """Пассивный AI игрок (рыба)"""
    def __init__(self):
        super().__init__("fish")
        self.aggression_factor = 0.3
        self.fold_threshold = 0.4
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        # Простая логика для fish AI
        return {"action": ActionType.CALL, "amount": 0}

class NitAI(BasePokerAI):
    """Сверхконсервативный AI игрок"""
    def __init__(self):
        super().__init__("nit")
        self.aggression_factor = 0.1
        self.fold_threshold = 0.9
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        return {"action": ActionType.FOLD, "amount": 0}