from typing import List
from pydantic import BaseModel


class UserBaseType(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class GroupBaseType(BaseModel):
    id: int
    group_name: str
    permissions: List["PermissionBaseType"]

    class Config:
        from_attributes = True


class PermissionBaseType(BaseModel):
    id: int
    permission_name: str

    class Config:
        from_attributes = True


class UserWithManagerType(UserBaseType):
    manager: UserBaseType | None


class UserWithPermissionType(UserBaseType):
    permissions: List[PermissionBaseType]
    groups: List[GroupBaseType]
