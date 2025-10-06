from app.database.database import init_db
from app.config import config

def main():
    print("Initializing Poker Mentor...")
    
    # Инициализация базы данных
    init_db()
    print("Database initialized successfully!")
    
    # Здесь позже добавим инициализацию бота и AI
    print(f"Configuration loaded: DEBUG={config.DEBUG}")

if __name__ == "__main__":
    main()