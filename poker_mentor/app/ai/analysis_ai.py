from app.ai.ai_client import ai_client
from app.ai.prompts.hand_analysis import HAND_ANALYSIS_PROMPT
from app.ai.prompts.training import TRAINING_PROMPT
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

class AnalysisAI:
    def __init__(self):
        self.kmeans = KMeans(n_clusters=5)
        self.fitted = False
    
    async def analyze_hand_history(self, hand_history: str, player_stats: dict) -> dict:
        """Анализ истории раздач"""
        prompt = HAND_ANALYSIS_PROMPT.format(
            hand_history=hand_history,
            player_stats=player_stats
        )
        
        analysis = await ai_client.get_completion(prompt)
        
        # Дополнительный ML анализ
        ml_insights = self._ml_analysis(hand_history)
        
        return {
            "ai_analysis": analysis,
            "ml_insights": ml_insights,
            "recommendations": self._generate_recommendations(ml_insights)
        }
    
    async def generate_training_content(self, topic: str, skill_level: str, aspects: list) -> dict:
        """Генерация обучающего контента"""
        prompt = TRAINING_PROMPT.format(
            topic=topic,
            skill_level=skill_level,
            aspects=", ".join(aspects)
        )
        
        content = await ai_client.get_completion(prompt)
        return {
            "topic": topic,
            "content": content,
            "exercises": self._generate_exercises(topic)
        }
    
    def _ml_analysis(self, hand_history: str) -> dict:
        """ML анализ паттернов в истории рук"""
        # Здесь будет преобразование истории в фичи для ML
        # Пока заглушка
        return {
            "aggression_factor": 0.75,
            "vpip": 0.25,
            "pfr": 0.18,
            "win_rate": 0.15
        }
    
    def _generate_recommendations(self, insights: dict) -> list:
        """Генерация рекомендаций на основе ML анализа"""
        recommendations = []
        
        if insights['aggression_factor'] < 0.5:
            recommendations.append("Увеличьте агрессию в игре")
        if insights['vpip'] > 0.3:
            recommendations.append("Снизьте количество раздач для входа в игру")
            
        return recommendations
    
    def _generate_exercises(self, topic: str) -> list:
        """Генерация упражнений по теме"""
        exercises = {
            "preflop": ["Ранг рук", "Позиционная игра", "Рестейки"],
            "postflop": ["Чтение борда", "Размеры ставок", "Блеф"],
            "bankroll": ["Управление банкроллом", "Выбор лимитов"]
        }
        
        return exercises.get(topic, ["Общие упражнения по покеру"])

# Глобальный инстанс Analysis AI
analysis_ai = AnalysisAI()