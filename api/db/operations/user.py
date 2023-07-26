from sqlalchemy.orm.session import Session
from db.models.user import PermissionModel, UserModel
from db.fixtures.permissions import permission_names

from db.values.user import UserCreateValues


def create_user(db: Session, user: UserCreateValues):
    new_user = UserModel(
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def reload_permissions(db: Session):
    for permission_name in permission_names:
        permission = (
            db.query(PermissionModel).filter_by(permission_name=permission_name).first()
        )
        if not permission:
            new_user = PermissionModel(
                permission_name=permission_name,
            )
            db.add(new_user)
    db.commit()
