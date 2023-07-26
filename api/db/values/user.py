from pydantic import BaseModel


class UserCreateValues(BaseModel):
    email: str
