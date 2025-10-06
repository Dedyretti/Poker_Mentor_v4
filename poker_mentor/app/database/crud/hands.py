from sqlalchemy.orm import Session
from app.database.models import HandHistory
from uuid import UUID

def create_hand_history(db: Session, session_id: UUID, hand_number: int, 
                       positions: dict, hole_cards: dict, actions: list):
    hand = HandHistory(
        session_id=session_id,
        hand_number=hand_number,
        positions=positions,
        hole_cards=hole_cards,
        actions=actions
    )
    db.add(hand)
    db.commit()
    db.refresh(hand)
    return hand

def get_hand_history_by_session(db: Session, session_id: UUID):
    return db.query(HandHistory).filter(HandHistory.session_id == session_id).all()

def update_hand_result(db: Session, hand_id: UUID, result: dict, analysis_data: dict = None):
    hand = db.query(HandHistory).filter(HandHistory.id == hand_id).first()
    if hand:
        hand.result = result
        if analysis_data:
            hand.analysis_data = analysis_data
        db.commit()
    return hand