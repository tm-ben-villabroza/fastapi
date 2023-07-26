from sqlalchemy.orm.session import Session
from db.types.user import UserWithManagerType, UserWithPermissionType
from schema.request.user import HasPermissionRequest
from db.models.user import PermissionModel, UserModel
from db.fixtures.permissions import permissions

from db.values.user import UserCreateValues


def create_user(db: Session, user: UserCreateValues):
    new_user = UserModel(
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def has_all_permission(
    db: Session, user: UserWithPermissionType, payload: HasPermissionRequest
):
    """
    checks user's permission based on groups and permissions table
    """
    all_user_permissions = set()
    missing_user_permissions = []

    # add permissions from permissions table
    for permission in user.permissions:
        all_user_permissions.add(permission.permission_name)

    # add permissions from permissions table associated via groups table
    for group in user.groups:
        for permission in group.permissions:
            all_user_permissions.add(permission.permission_name)

    for permission_name in payload.permission_names:
        if permission_name not in all_user_permissions:
            missing_user_permissions.append(permission_name)

    if missing_user_permissions:
        return "INSUFFICIENT_PERMISSIONS", missing_user_permissions
    return "SUFFICIENT_PERMISSIONS", []


def reload_permissions(db: Session):
    for permission in permissions.values():
        permission_name = permission["permission_name"]
        permission_db = (
            db.query(PermissionModel).filter_by(permission_name=permission_name).first()
        )
        if not permission_db:
            new_permission = PermissionModel(
                permission_name=permission_name,
            )
            db.add(new_permission)
    db.commit()
