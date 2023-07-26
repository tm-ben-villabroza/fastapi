from sqlalchemy.orm.session import Session
from db.models.user import UserModel

from db.values.user import UserCreateValues


def create_user(db: Session, user: UserCreateValues):
    new_user = UserModel(
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
