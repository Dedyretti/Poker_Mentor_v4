from sqlalchemy import Column, String, Integer, DateTime, Boolean, JSON, ForeignKey, Text, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import enum

Base = declarative_base()

class SkillLevel(enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class GameType(enum.Enum):
    CASH = "cash"
    TOURNAMENT = "tournament"

class SessionStatus(enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class AIType(enum.Enum):
    FISH = "fish"
    TAG = "tag"
    LAG = "lag"
    NIT = "nit"

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(String(100), unique=True, nullable=False, index=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    registration_date = Column(DateTime, default=datetime.utcnow)
    skill_level = Column(SQLEnum(SkillLevel), default=SkillLevel.BEGINNER)
    preferences = Column(JSON, default=dict)
    is_active = Column(Boolean, default=True)
    last_activity = Column(DateTime, default=datetime.utcnow)

class GameSession(Base):
    __tablename__ = "game_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    game_type = Column(SQLEnum(GameType), default=GameType.CASH)
    stake_level = Column(String(50), default="1/2")
    stack_size = Column(Integer, default=1000)
    ai_type = Column(SQLEnum(AIType), default=AIType.FISH)
    created_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime)
    status = Column(SQLEnum(SessionStatus), default=SessionStatus.ACTIVE)
    session_data = Column(JSON, default=dict)  # Текущее состояние игры

class HandHistory(Base):
    __tablename__ = "hand_histories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("game_sessions.id"), nullable=False, index=True)
    hand_number = Column(Integer, nullable=False)
    positions = Column(JSON, nullable=False)  # Позиции игроков за столом
    hole_cards = Column(JSON, nullable=False)  # Карты игрока
    community_cards = Column(JSON, default=dict)  # Карты на столе
    actions = Column(JSON, nullable=False)  # История действий
    result = Column(JSON)  # Результат раздачи
    analysis_data = Column(JSON)  # Данные анализа от AI
    hand_strength = Column(String(50))  # Сила руки (префлоп)
    created_at = Column(DateTime, default=datetime.utcnow)

class AIProfile(Base):
    __tablename__ = "ai_profiles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(SQLEnum(AIType), nullable=False)
    parameters = Column(JSON, nullable=False)  # Параметры поведения AI
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)