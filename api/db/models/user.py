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

group_permissions = Table(
    "group_permissions",
    BaseModel.metadata,
    Column("group_id", ForeignKey("groups.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "permission_id",
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

user_groups = Table(
    "user_groups",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "group_id",
        ForeignKey("groups.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    permissions: Mapped[List["PermissionModel"]] = relationship(
        secondary=user_permissions, back_populates="users"
    )
    groups: Mapped[List["GroupModel"]] = relationship(
        secondary=user_groups, back_populates="users"
    )
    manager_id = mapped_column(Integer, ForeignKey("users.id"))
    manager = relationship("UserModel", back_populates="subordinates", remote_side=[id])
    subordinates = relationship("UserModel", back_populates="manager")
    email = Column(String(60))


class PermissionModel(BaseModel):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    users: Mapped[List[UserModel]] = relationship(
        secondary=user_permissions, back_populates="permissions"
    )
    groups: Mapped[List["GroupModel"]] = relationship(
        secondary=group_permissions, back_populates="permissions"
    )
    permission_name = Column(String(60))


class GroupModel(BaseModel):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    users: Mapped[List[UserModel]] = relationship(
        secondary=user_groups, back_populates="groups"
    )
    permissions: Mapped[List[PermissionModel]] = relationship(
        secondary=group_permissions, back_populates="groups"
    )
    group_name = Column(String(60))
