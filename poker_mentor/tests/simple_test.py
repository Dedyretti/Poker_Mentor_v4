# Простой тест без сложных импортов
import random

class Card :
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f"{self.rank}{self.suit[0].upper()}"

class Deck :
    def __init__(self):
        self.cards = []
        self.reset()
    
    def reset(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop() if self.cards else None

# Тест
deck = Deck()
print(f"Deck created with {len(deck.cards)} cards")
card1 = deck.deal()
card2 = deck.deal()
print(f"Dealt {card1}, {card2}")
print(f"Remaining {len(deck.cards)} cards")