from abc import ABC, abstractmethod
from typing import Dict, List
from app.game.engine import ActionType

class BasePokerAI(ABC):
    """Базовый класс для всех AI игроков"""
    
    def __init__(self, ai_type: str, name: str = "AI"):
        self.ai_type = ai_type
        self.name = name
        self.aggression_factor = 1.0
        self.fold_threshold = 0.7
        self.call_threshold = 0.5
    
    @abstractmethod
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        """Принять решение о действии"""
        pass
    
    def calculate_hand_strength(self, hole_cards: List, community_cards: List) -> float:
        """Рассчитать силу руки (упрощенная версия)"""
        # Базовая оценка силы руки
        if not hole_cards:
            return 0.0
        
        # Простая эвристика для демонстрации
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        
        if len(hole_cards) == 2:
            card1_val = card_values.get(hole_cards[0].rank, 0)
            card2_val = card_values.get(hole_cards[1].rank, 0)
            
            # Пара
            if hole_cards[0].rank == hole_cards[1].rank:
                return min(0.8, card1_val / 20 + 0.3)
            
            # Одинаковая масть
            if hole_cards[0].suit == hole_cards[1].suit:
                return min(0.6, (card1_val + card2_val) / 40 + 0.2)
            
            # Разные масти
            return (card1_val + card2_val) / 40
        
        return 0.5

class FishAI(BasePokerAI):
    """Пассивный AI игрок (рыба) - играет много рук, редко рейзит"""
    
    def __init__(self):
        super().__init__("fish", "AI_Fish")
        self.aggression_factor = 0.3
        self.fold_threshold = 0.2
        self.call_threshold = 0.3
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        hand_strength = self.calculate_hand_strength(hole_cards, game_state.get('community_cards', []))
        
        # Рыба редко фолдит и редко рейзит
        if hand_strength < self.fold_threshold:
            return {"action": ActionType.FOLD, "amount": 0}
        elif hand_strength > 0.7:
            return {"action": ActionType.RAISE, "amount": game_state.get('current_bet', 20) * 2}
        else:
            return {"action": ActionType.CALL, "amount": 0}

class NitAI(BasePokerAI):
    """Сверхконсервативный AI игрок - играет только премиум руки"""
    
    def __init__(self):
        super().__init__("nit", "AI_Nit")
        self.aggression_factor = 0.1
        self.fold_threshold = 0.8
        self.call_threshold = 0.7
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        hand_strength = self.calculate_hand_strength(hole_cards, game_state.get('community_cards', []))
        
        # Нит фолдит почти всегда, кроме очень сильных рук
        if hand_strength < self.fold_threshold:
            return {"action": ActionType.FOLD, "amount": 0}
        elif hand_strength > 0.9:
            return {"action": ActionType.RAISE, "amount": game_state.get('current_bet', 20) * 3}
        else:
            return {"action": ActionType.CALL, "amount": 0}

class TAGAI(BasePokerAI):
    """Тайтово-агрессивный AI - играет мало рук, но агрессивно"""
    
    def __init__(self):
        super().__init__("tag", "AI_TAG")
        self.aggression_factor = 0.8
        self.fold_threshold = 0.6
        self.call_threshold = 0.5
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        hand_strength = self.calculate_hand_strength(hole_cards, game_state.get('community_cards', []))
        
        if hand_strength < self.fold_threshold:
            return {"action": ActionType.FOLD, "amount": 0}
        elif hand_strength > 0.5:
            return {"action": ActionType.RAISE, "amount": game_state.get('current_bet', 20) * 2}
        else:
            return {"action": ActionType.CALL, "amount": 0}

class LAGAI(BasePokerAI):
    """Лузово-агрессивный AI - играет много рук, очень агрессивно"""
    
    def __init__(self):
        super().__init__("lag", "AI_LAG")
        self.aggression_factor = 0.9
        self.fold_threshold = 0.1
        self.call_threshold = 0.2
    
    async def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        hand_strength = self.calculate_hand_strength(hole_cards, game_state.get('community_cards', []))
        
        # LAG почти никогда не фолдит и часто рейзит
        if hand_strength < self.fold_threshold:
            return {"action": ActionType.FOLD, "amount": 0}
        elif hand_strength > 0.3:
            return {"action": ActionType.RAISE, "amount": game_state.get('current_bet', 20) * 3}
        else:
            return {"action": ActionType.CALL, "amount": 0}