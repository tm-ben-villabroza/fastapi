from datetime import datetime
from pydantic import BaseModel

from schema.helpers.emotion import EmotionName


class EmotionResponse(BaseModel):
    id: int
    name: EmotionName
    create_datetime: datetime

    class Config:
        from_attributes = True
