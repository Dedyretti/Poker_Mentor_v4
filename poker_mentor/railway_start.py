# railway_start.py - альтернативная точка входа для продакшена
import os
from app.bot.webhook_server import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)