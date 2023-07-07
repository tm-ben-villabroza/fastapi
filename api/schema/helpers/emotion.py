from enum import Enum
from pydantic import BaseModel

class EmotionName(str, Enum):
    happy = 'happy'
    inspired = 'inspired'
    sad = 'sad'
    dissatisfied = 'dissatisfied'
    annoyed = 'annoyed'
    afraid = 'afraid'
    angry = 'angry'
    bored = 'bored'