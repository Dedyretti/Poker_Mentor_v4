from typing import List, Dict
from .poker_logic import Card, Deck
from .player import Player

class PokerTable:
    def __init__(self, table_id: str, blinds: Dict[str, int] = None):
        self.table_id = table_id
        self.blinds = blinds or {"small": 1, "big": 2}
        self.players: List[Player] = []
        self.deck = Deck()
        self.community_cards: List[Card] = []
        self.pot = 0
        self.current_bet = 0
        self.dealer_position = 0
        
    def add_player(self, player: Player):
        self.players.append(player)
    
    def start_hand(self):
        """Начинает новую раздачу"""
        self.deck.reset()
        self.community_cards = []
        self.pot = 0
        self.current_bet = self.blinds["big"]
        
        # Сбрасываем состояние игроков
        for player in self.players:
            player.reset_hand()
            player.receive_cards([self.deck.deal(), self.deck.deal()])
    
    def deal_flop(self):
        """Раздает флоп (3 карты)"""
        self.deck.deal()  # Сжигаем карту
        self.community_cards.extend([self.deck.deal() for _ in range(3)])
    
    def deal_turn(self):
        """Раздает терн (4-я карта)"""
        self.deck.deal()  # Сжигаем карту
        self.community_cards.append(self.deck.deal())
    
    def deal_river(self):
        """Раздает ривер (5-я карта)"""
        self.deck.deal()  # Сжигаем карту
        self.community_cards.append(self.deck.deal())