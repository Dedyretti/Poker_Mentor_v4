import sys
import os

# Добавляем корень проекта в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from app.game.poker_logic import Deck, Card
from app.game.table import PokerTable
from app.game.player import Player

def test_deck():
    print("Testing Deck...")
    deck = Deck()
    print(f"Deck has {len(deck.cards)} cards")
    
    # Проверяем раздачу карт
    card1 = deck.deal()
    card2 = deck.deal()
    print(f"Dealt cards: {card1}, {card2}")
    print(f"Remaining cards: {len(deck.cards)}")

def test_players():
    print("\nTesting Players...")
    player1 = Player("1", "Player 1", 1000)
    player2 = Player("2", "Player 2", 1000)
    
    # Тест получения карт
    deck = Deck()
    player1.receive_cards([deck.deal(), deck.deal()])
    player2.receive_cards([deck.deal(), deck.deal()])
    
    print(f"Player 1 cards: {player1.hole_cards}")
    print(f"Player 2 cards: {player2.hole_cards}")
    
    # Тест ставок
    player1.place_bet(100)
    print(f"Player 1 bet: {player1.current_bet}, stack: {player1.stack}")

def test_table():
    print("\nTesting Table...")
    table = PokerTable("test_table")
    player1 = Player("1", "Player 1")
    player2 = Player("2", "Player 2")
    
    table.add_player(player1)
    table.add_player(player2)
    
    table.start_hand()
    
    print(f"Community cards: {table.community_cards}")
    print(f"Pot: {table.pot}")

if __name__ == "__main__":
    test_deck()
    test_players()
    test_table()
    print("\nAll tests passed! ✅")