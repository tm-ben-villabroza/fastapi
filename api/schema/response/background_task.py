from datetime import datetime
from typing import Any
from pydantic import BaseModel

from schema.helpers.emotion import EmotionName


class StatusResponse(BaseModel):
    status: str
    result: Any


class DivideResponse(BaseModel):
    id: str
