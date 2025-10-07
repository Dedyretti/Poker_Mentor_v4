import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from app.game.engine import PokerEngine, ActionType
from app.game.table import PokerTable
from app.game.player import Player

def test_engine():
    print("Testing Poker Engine...")
    
    # Создаем стол и игроков
    table = PokerTable("test_table", {"small": 5, "big": 10})
    player1 = Player("1", "Alice", 1000)
    player2 = Player("2", "Bob", 1000)
    
    table.add_player(player1)
    table.add_player(player2)
    
    # Создаем движок
    engine = PokerEngine(table)
    
    # Начинаем раздачу
    engine.start_new_hand()
    
    print("Initial game state:")
    state = engine.get_game_state()
    print(f"State: {state['state']}")
    print(f"Current player: {state['current_player']}")
    print(f"Players: {[p['name'] for p in state['players']]}")
    
    # Симулируем несколько действий
    print("\n--- Simulating actions ---")
    
    # Игрок 1 коллирует блайнды
    engine.process_player_action(ActionType.CALL, 10)
    print(f"After call: {engine.get_game_state()['current_player']}")
    
    # Игрок 2 чекает
    engine.process_player_action(ActionType.CHECK)
    print(f"After check: Flop should be dealt")
    
    print("\nFinal game state:")
    final_state = engine.get_game_state()
    for key, value in final_state.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_engine()