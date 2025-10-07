import sys
import os

# Добавляем корневую директорию в путь для импортов
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    """Основная функция запуска приложения"""
    print("🎯 Запуск Poker Mentor v4...")
    
    # Для разработки используем polling, для продакшена - webhook
    use_webhook = os.getenv('USE_WEBHOOK', 'False').lower() == 'true'
    
    try:
        from app.bot.bot_core import start_bot
        start_bot(use_webhook=use_webhook)
    except KeyboardInterrupt:
        print("\n⏹️ Приложение остановлено")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()