from datetime import datetime
from typing import List

from sqlalchemy import Table, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import BaseModel

user_permissions = Table(
    "user_permissions",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "permission_id",
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    permissions: Mapped[List["PermissionModel"]] = relationship(
        secondary=user_permissions, back_populates="users"
    )
    email = Column(String(60))


class PermissionModel(BaseModel):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    users: Mapped[List[UserModel]] = relationship(
        secondary=user_permissions, back_populates="permissions"
    )
    permission_name = Column(String(60))
