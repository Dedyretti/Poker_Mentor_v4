from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import config
from .models import Base

# Создаем движок базы данных
engine = create_engine(config.DATABASE_URL)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Инициализация базы данных - создание таблиц"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Получение сессии базы данных для зависимостей"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()