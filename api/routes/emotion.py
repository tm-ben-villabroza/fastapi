from db.database import get_db
from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from schema.request.emotion import EmotionCreateRequest, EmotionReadRequest
from db.operations import emotion as emotion_op
from schema.response.emotion import EmotionResponse

router = APIRouter(prefix="/emotion", tags=["emotion"])


@router.post("/create", response_model=EmotionResponse)
def create_emotion(emotion: EmotionCreateRequest, db: Session = Depends(get_db)):
    return emotion_op.create_emotion(db, emotion)


@router.post("/read", response_model=List[EmotionResponse])
def read_emotion(emotion: EmotionReadRequest, db: Session = Depends(get_db)):
    return emotion_op.read_emotion(db, emotion)


@router.get("/read/all", response_model=List[EmotionResponse])
def read_emotion_all(db: Session = Depends(get_db)):
    return emotion_op.read_emotion_all(db)
