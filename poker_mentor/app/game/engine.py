import enum
from typing import List, Dict, Optional
from .poker_logic import Deck, Card, PokerHand
from .table import PokerTable
from .player import Player

class GameState(enum.Enum):
    WAITING = "waiting"
    PREFLOP = "preflop"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"
    SHOWDOWN = "showdown"
    COMPLETED = "completed"

class ActionType(enum.Enum):
    FOLD = "fold"
    CHECK = "check"
    CALL = "call"
    RAISE = "raise"
    ALL_IN = "all_in"

class PokerEngine:
    def __init__(self, table: PokerTable, ai_players: List = None):
        self.table = table
        self.state = GameState.WAITING
        self.current_player_index = 0
        self.hand_number = 0
        self.action_history = []
        self.ai_players = ai_players or []
    
    def add_ai_player(self, ai):
        """Добавляет AI игрока"""
        self.ai_players.append(ai)
    
    def start_new_hand(self):
        """Начинает новую раздачу"""
        self.hand_number += 1
        self.state = GameState.PREFLOP
        self.current_player_index = 0
        self.action_history = []
        
        self.table.start_hand()
        print(f"Started hand #{self.hand_number}")
    
    def get_current_player(self) -> Optional[Player]:
        """Возвращает текущего активного игрока"""
        active_players = [p for p in self.table.players if p.is_active]
        if not active_players:
            return None
        return active_players[self.current_player_index % len(active_players)]
    
    def process_player_action(self, action: ActionType, amount: int = 0) -> bool:
        """Обрабатывает действие игрока"""
        player = self.get_current_player()
        if not player:
            return False
        
        print(f"Player {player.name} action: {action.value}, amount: {amount}")
        
        if action == ActionType.FOLD:
            player.fold()
            self.action_history.append({
                "player": player.player_id,
                "action": "fold",
                "amount": 0
            })
        
        elif action == ActionType.CHECK:
            if player.current_bet < self.table.current_bet:
                return False
            self.action_history.append({
                "player": player.player_id,
                "action": "check",
                "amount": 0
            })
        
        elif action == ActionType.CALL:
            call_amount = self.table.current_bet - player.current_bet
            if call_amount > player.stack:
                return False
            player.place_bet(call_amount)
            self.table.pot += call_amount
            self.action_history.append({
                "player": player.player_id,
                "action": "call",
                "amount": call_amount
            })
        
        elif action == ActionType.RAISE:
            if amount <= self.table.current_bet:
                return False
            if amount > player.stack:
                return False
            
            player.place_bet(amount - player.current_bet)
            self.table.pot += (amount - player.current_bet)
            self.table.current_bet = amount
            self.action_history.append({
                "player": player.player_id,
                "action": "raise",
                "amount": amount
            })
        
        self.current_player_index += 1
        
        if self._is_round_complete():
            self._advance_street()
        
        return True
    
    def process_ai_turn(self):
        """Обрабатывает ход AI игрока"""
        current_player = self.get_current_player()
        if not current_player:
            return False
        
        ai_player = self._get_ai_for_player(current_player.player_id)
        if not ai_player:
            return False
        
        # Импортируем здесь чтобы избежать циклических импортов
        from app.ai.game_ai import BasePokerAI
        if isinstance(ai_player, BasePokerAI):
            game_state = self.get_game_state()
            action_data = ai_player.decide_action(game_state, current_player.hole_cards)
            
            success = self.process_player_action(
                action_data["action"], 
                action_data.get("amount", 0)
            )
            
            if success:
                print(f"AI {current_player.name} action: {action_data['action'].value}")
            
            return success
        return False
    
    def _get_ai_for_player(self, player_id: str):
        """Находит AI для игрока"""
        return self.ai_players[0] if self.ai_players else None
    
    def _is_round_complete(self) -> bool:
        """Проверяет, завершился ли текущий раунд торгов"""
        active_players = [p for p in self.table.players if p.is_active and not p.is_all_in]
        
        if len(active_players) <= 1:
            return True
        
        current_bets = [p.current_bet for p in active_players]
        return all(bet == current_bets[0] for bet in current_bets)
    
    def _advance_street(self):
        """Переход к следующей улице"""
        if self.state == GameState.PREFLOP:
            self.state = GameState.FLOP
            self.table.deal_flop()
            print("Flop dealt:", self.table.community_cards)
        
        elif self.state == GameState.FLOP:
            self.state = GameState.TURN
            self.table.deal_turn()
            print("Turn dealt:", self.table.community_cards[-1])
        
        elif self.state == GameState.TURN:
            self.state = GameState.RIVER
            self.table.deal_river()
            print("River dealt:", self.table.community_cards[-1])
        
        elif self.state == GameState.RIVER:
            self.state = GameState.SHOWDOWN
            self._determine_winner()
        
        for player in self.table.players:
            player.current_bet = 0
        self.table.current_bet = self.table.blinds["big"]
        self.current_player_index = 0
    
    def _determine_winner(self):
        """Определяет победителя раздачи"""
        active_players = [p for p in self.table.players if p.is_active]
        
        if len(active_players) == 1:
            winner = active_players[0]
            winner.stack += self.table.pot
            print(f"Player {winner.name} wins {self.table.pot} (all others folded)")
        else:
            best_hand = None
            winners = []
            
            for player in active_players:
                all_cards = player.hole_cards + self.table.community_cards
                hand_rank, strength, combo_cards = PokerHand.evaluate_hand(all_cards)
                
                if not best_hand or strength > best_hand[1]:
                    best_hand = (hand_rank, strength, combo_cards)
                    winners = [player]
                elif strength == best_hand[1]:
                    winners.append(player)
            
            prize = self.table.pot // len(winners)
            for winner in winners:
                winner.stack += prize
                print(f"Player {winner.name} wins {prize} with {best_hand[0]}")
        
        self.state = GameState.COMPLETED
    
    def get_game_state(self) -> Dict:
        """Возвращает текущее состояние игры для отображения"""
        current_player = self.get_current_player()
        return {
            "hand_number": self.hand_number,
            "state": self.state.value,
            "current_player": current_player.name if current_player else None,
            "community_cards": [str(card) for card in self.table.community_cards],
            "pot": self.table.pot,
            "players": [
                {
                    "name": p.name,
                    "stack": p.stack,
                    "current_bet": p.current_bet,
                    "is_active": p.is_active,
                    "is_all_in": p.is_all_in,
                    "hole_cards": [str(card) for card in p.hole_cards] if p.is_active else []
                }
                for p in self.table.players
            ],
            "action_history": self.action_history[-10:]
        }