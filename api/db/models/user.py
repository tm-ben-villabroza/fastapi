from datetime import datetime
from typing import List

from sqlalchemy import Table, Column, ForeignKey, String, Integer
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
    manager_id = mapped_column(Integer, ForeignKey("users.id"))
    subordinate = relationship("UserModel", back_populates="manager")
    manager = relationship("UserModel", back_populates="subordinate", remote_side=[id])
    email = Column(String(60))


class PermissionModel(BaseModel):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    users: Mapped[List[UserModel]] = relationship(
        secondary=user_permissions, back_populates="permissions"
    )
    permission_name = Column(String(60))
