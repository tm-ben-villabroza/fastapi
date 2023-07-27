from db.types.user import UserBaseType, UserWithManagerType
from .decorators.auth import require_authentication
from db.database import get_db
from fastapi import APIRouter, Request
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from schema.request.emotion import EmotionCreateRequest, EmotionReadRequest
from db.operations import emotion as emotion_op
from schema.response.emotion import EmotionResponse

router = APIRouter(prefix="/emotion", tags=["emotion"])


@router.post("/create", response_model=EmotionResponse)
@require_authentication
async def create_emotion(
    request: Request,
    emotion: EmotionCreateRequest,
    db: Session = Depends(get_db),
    user: UserWithManagerType = None,
):
    return emotion_op.create_emotion(db, emotion)


@router.post("/read", response_model=List[EmotionResponse])
@require_authentication
async def read_emotion(
    request: Request,
    emotion: EmotionReadRequest,
    db: Session = Depends(get_db),
    user: UserWithManagerType = None,
):
    return emotion_op.read_emotion(db, emotion)


@router.get("/read/all", response_model=List[EmotionResponse])
@require_authentication
async def read_emotion_all(
    request: Request, db: Session = Depends(get_db), user: UserBaseType = None
):
    print(user.email)
    print(user.id)
    if user.manager:
        print(user.manager.email)
    return emotion_op.read_emotion_all(db)
