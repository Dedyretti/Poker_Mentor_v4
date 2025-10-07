import random
from typing import List, Dict, Tuple

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank  # '2', '3', ..., 'A'
        self.suit = suit  # 'hearts', 'diamonds', 'clubs', 'spades'
    
    def __repr__(self):
        return f"{self.rank}{self.suit[0].upper()}"

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()
    
    def reset(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self) -> Card:
        return self.cards.pop() if self.cards else None

class PokerHand:
    HAND_RANKS = {
        "high_card": 1,
        "pair": 2,
        "two_pairs": 3,
        "three_of_a_kind": 4,
        "straight": 5,
        "flush": 6,
        "full_house": 7,
        "four_of_a_kind": 8,
        "straight_flush": 9,
        "royal_flush": 10
    }
    
    @staticmethod
    def evaluate_hand(cards: List[Card]) -> Tuple[str, int, List[Card]]:
        """
        Оценивает силу руки и возвращает:
        - название комбинации
        - сила руки (число)
        - карты, составляющие комбинацию
        """
        if len(cards) < 5:
            return "not_enough_cards", 0, []
        
        # Здесь будет логика определения комбинаций
        # Пока заглушка - определяем только старшую карту
        sorted_cards = sorted(cards, key=lambda x: PokerHand.rank_to_value(x.rank), reverse=True)
        return "high_card", PokerHand.rank_to_value(sorted_cards[0].rank), [sorted_cards[0]]
    
    @staticmethod
    def rank_to_value(rank: str) -> int:
        rank_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return rank_values.get(rank, 0)
    
    @staticmethod
    def compare_hands(hand1: List[Card], hand2: List[Card]) -> int:
        """
        Сравнивает две руки и возвращает:
        -1 если hand1 слабее hand2
         0 если равны
         1 если hand1 сильнее hand2
        """
        rank1, strength1, _ = PokerHand.evaluate_hand(hand1)
        rank2, strength2, _ = PokerHand.evaluate_hand(hand2)
        
        if strength1 > strength2:
            return 1
        elif strength1 < strength2:
            return -1
        else:
            return 0