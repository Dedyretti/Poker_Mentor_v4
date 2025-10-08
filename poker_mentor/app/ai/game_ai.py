import torch
import torch.nn as nn
import numpy as np
from app.ai.ai_client import ai_client
from app.ai.prompts.game_play import GAME_DECISION_PROMPT, HAND_STRENGTH_PROMPT

class PokerDecisionModel(nn.Module):
    """Локальная ML модель для принятия покерных решений"""
    def __init__(self, input_size=128, hidden_size=256, output_size=4):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.network(x)

class GameAI:
    def __init__(self):
        self.local_model = PokerDecisionModel()
        self.model_loaded = False
        
    async def get_game_decision(self, game_state: dict) -> dict:
        """Получить рекомендацию по ходу игры"""
        prompt = GAME_DECISION_PROMPT.format(**game_state)
        response = await ai_client.get_completion(prompt, temperature=0.3)
        
        # Парсинг ответа
        lines = response.split('\n')
        decision = {"action": "fold", "reason": "Базовая рекомендация"}
        
        for line in lines:
            if line.startswith('ДЕЙСТВИЕ:'):
                decision['action'] = line.split(':')[1].strip().lower()
            elif line.startswith('ОБОСНОВАНИЕ:'):
                decision['reason'] = line.split(':')[1].strip()
                
        return decision
    
    async def analyze_hand_strength(self, cards: list, community_cards: list, player_count: int) -> dict:
        """Анализ силы руки"""
        prompt = HAND_STRENGTH_PROMPT.format(
            player_cards=cards,
            community_cards=community_cards,
            player_count=player_count
        )
        
        analysis = await ai_client.get_completion(prompt)
        return {"analysis": analysis}

# Глобальный инстанс Game AI
game_ai = GameAI()