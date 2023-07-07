from sqlalchemy.orm.session import Session
from db.models.emotion import EmotionModel

from schema.request.emotion import EmotionCreateRequest, EmotionReadRequest


def create_emotion(db: Session, emotion: EmotionCreateRequest):
    new_emotion = EmotionModel(
      name=emotion.name,
    )
    db.add(new_emotion)
    db.commit()
    db.refresh(new_emotion)
    return new_emotion


def read_emotion(db: Session, emotion: EmotionReadRequest):
    return db.query(EmotionModel).filter(EmotionModel.id == emotion.id).all()


def read_emotion_all(db: Session):
    return db.query(EmotionModel).all()
