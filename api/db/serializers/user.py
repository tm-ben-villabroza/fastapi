from pydantic import BaseModel


class UserSerializer(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
