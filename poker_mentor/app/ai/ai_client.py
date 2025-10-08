import openai
from openai import AsyncOpenAI
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class AIClient:  # ✅ ИСПРАВЛЕНО: AIClient вместо AIClientry
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)  # ✅ = вместо -
        self.model = settings.OPENAI_MODEL
        
    async def get_completion(self, prompt: str, temperature: float = 0.7) -> str:
        """Получение ответа от OpenAI API"""  # ✅ Исправлено описание
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
    
    async def get_embedding(self, text: str) -> list:
        """Получение эмбеддингов для текста"""  # ✅ Исправлено описание
        try:
            response = await self.client.embeddings.create(
                model="text-embedding-ada-002",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"OpenAI Embedding error: {e}")
            return []

# Глобальный инстанс AI клиента
ai_client = AIClient()  # ✅ AIClient вместо AIClientry