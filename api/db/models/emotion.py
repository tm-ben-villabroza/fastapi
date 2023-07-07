from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from ..database import BaseModel


class EmotionModel(BaseModel):
    __tablename__ = "emotions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    create_datetime = Column(DateTime, default=datetime.now)
