from sqlalchemy.orm import Session
from app.database.models import GameSession, SessionStatus
from uuid import UUID
from datetime import datetime

def create_game_session(db: Session, user_id: UUID, game_type: str = "cash", 
                       stake_level: str = "1/2", stack_size: int = 1000, ai_type: str = "fish"):
    session = GameSession(
        user_id=user_id,
        game_type=game_type,
        stake_level=stake_level,
        stack_size=stack_size,
        ai_type=ai_type
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def get_active_session(db: Session, user_id: UUID):
    return db.query(GameSession).filter(
        GameSession.user_id == user_id,
        GameSession.status == SessionStatus.ACTIVE
    ).first()

def complete_session(db: Session, session_id: UUID):
    session = db.query(GameSession).filter(GameSession.id == session_id).first()
    if session:
        session.status = SessionStatus.COMPLETED
        session.ended_at = datetime.utcnow()
        db.commit()
    return session