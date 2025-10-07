import random
from typing import Dict, List

class BasePokerAI:
    def __init__(self, difficulty: str = "easy"):
        self.difficulty = difficulty
    
    def decide_action(self, game_state: Dict, hole_cards: List) -> Dict:
        """Принимает решение о действии"""
        # Простая логика для тестирования
        actions = ["fold", "check", "call", "raise"]
        weights = [0.1, 0.3, 0.4, 0.2]  # Вероятности действий
        
        action = random.choices(actions, weights=weights)[0]
        amount = 0
        
        if action == "raise":
            amount = random.randint(20, 100)
        
        return {
            "action": action,
            "amount": amount
        }