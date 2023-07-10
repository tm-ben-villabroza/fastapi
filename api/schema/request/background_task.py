from pydantic import BaseModel


class StatusRequest(BaseModel):
    id: str


class DivideRequest(BaseModel):
    x: float
    y: float
    delay: int
