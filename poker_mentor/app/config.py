import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Webhook Configuration
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://your-domain.com')  # Замените на ваш URL
WEBHOOK_PATH = f"/webhook/{TELEGRAM_BOT_TOKEN}"

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./poker_mentor.db')

# AI Configuration
AI_API_KEY = os.getenv('AI_API_KEY')
AI_MODEL = os.getenv('AI_MODEL', 'gpt-4')

# Game Configuration
DEFAULT_STACK = int(os.getenv('DEFAULT_STACK', '1000'))
DEFAULT_BLIND = int(os.getenv('DEFAULT_BLIND', '10'))