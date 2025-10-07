from typing import List, Dict, Optional
from .poker_logic import Card

class Player:
    def __init__(self, player_id: str, name: str, stack: int = 1000):
        self.player_id = player_id
        self.name = name
        self.stack = stack
        self.hole_cards: List[Card] = []
        self.current_bet = 0
        self.is_active = True
        self.is_all_in = False
    
    def reset_hand(self):
        self.hole_cards = []
        self.current_bet = 0
        self.is_active = True
        self.is_all_in = False
    
    def receive_cards(self, cards: List[Card]):
        self.hole_cards.extend(cards)
    
    def place_bet(self, amount: int) -> bool:
        if amount > self.stack:
            return False
        
        self.stack -= amount
        self.current_bet += amount
        
        if self.stack == 0:
            self.is_all_in = True
        
        return True
    
    def fold(self):
        self.is_active = False
        self.hole_cards = []