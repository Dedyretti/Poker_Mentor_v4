import openai
from openai import AsyncOpenAI
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class AIClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
        
    async def get_completion(self, prompt: str, temperature: float = 0.7) -> str:
        """Получение ответа от OpenAI API"""
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return "Извините, сервис временно недоступен"

# Глобальный инстанс AI клиента
ai_client = AIClient()