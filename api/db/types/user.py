from pydantic import BaseModel


class UserBaseType(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserWithManagerType(UserBaseType):
    manager: UserBaseType
