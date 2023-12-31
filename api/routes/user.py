from schema.request.user import HasPermissionRequest
from db.types.user import UserBaseType, UserWithManagerType
from .decorators.auth import require_authentication
from db.database import get_db
from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from fastapi import Depends
from db.operations import user as user_op
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/permissions/has-all-permissions")
@require_authentication
async def has_all_permission(
    request: Request,
    payload: HasPermissionRequest,
    db: Session = Depends(get_db),
    user: UserWithManagerType = None,
):
    status, missing_permissions = user_op.has_all_permission(db, user, payload)
    return {"status": status, "missing_permissions": missing_permissions}


@router.post("/permissions/reload")
@require_authentication
async def create_emotion(
    request: Request,
    db: Session = Depends(get_db),
    user: UserWithManagerType = None,
):
    if user.email == "benv@thinkingmachin.es":
        user_op.reload_permissions(db)
        return {"status": "success"}
    else:
        raise HTTPException(
            detail={"message": "No authorization to this endpoint"}, status_code=401
        )
