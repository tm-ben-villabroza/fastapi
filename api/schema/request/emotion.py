from pydantic import BaseModel

from schema.helpers.emotion import EmotionName


class EmotionCreateRequest(BaseModel):
    name: EmotionName


class EmotionReadRequest(BaseModel):
    id: int
