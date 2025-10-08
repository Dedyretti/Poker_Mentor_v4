import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

async def test_integration():
    print("🧪 Testing integration...")
    
    # Тест базы данных
    try:
        from app.database.database import init_db
        init_db()
        print("✅ Database: OK")
    except Exception as e:
        print(f"❌ Database: {e}")
    
    # Тест AI
    try:
        from app.ai.ai_client import AIClient
        ai = AIClient()
        print("✅ AI Client: OK")
    except Exception as e:
        print(f"❌ AI Client: {e}")
    
    # Тест игровой логики
    try:
        from app.game.game_service import game_service
        print("✅ Game Service: OK")
    except Exception as e:
        print(f"❌ Game Service: {e}")
    
    # Тест бота
    try:
        from app.bot.bot_core import setup_handlers
        print("✅ Bot Handlers: OK")
    except Exception as e:
        print(f"❌ Bot Handlers: {e}")

if __name__ == "__main__":
    asyncio.run(test_integration())